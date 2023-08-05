# coding=utf-8
"""
Filesystem functions.
"""
import logging
import json
import re
import sys
from datetime import datetime
from pathlib import Path
import hashlib


def _hash_bytestr_iter(bytes_iter: bytes, hashing_function, as_hex_str=False):
    for block in bytes_iter:
        hashing_function.update(block)
    return hashing_function.hexdigest() if as_hex_str else hashing_function.digest()


def _file_as_blockiter(file, block_size=65536) -> bytes:
    with file:
        block = file.read(block_size)
        while len(block) > 0:
            yield block
            block = file.read(block_size)


def get_file_dict(path: (Path, str)) -> dict:
    """
    return hash, fs time and file size for a given file.
    :param path:
    :return:
    """
    p = Path(path) if isinstance(path, str) else path
    if p.exists():
        atime = datetime.fromtimestamp(p.stat().st_atime)
        ctime = datetime.fromtimestamp(p.stat().st_ctime)
        mtime = datetime.fromtimestamp(p.stat().st_mtime)
        size = p.stat().st_size
        file_hash = _hash_bytestr_iter(_file_as_blockiter(p.open(mode="rb")), hashlib.sha256())
        return {"file": path, "hash": file_hash,
                "atime": atime, "ctime": ctime, "mtime": mtime, "size": size
                }
    else:
        raise FileNotFoundError("%s does not exist." % path)


def is_excluded(path: (Path, str), excluded_paths) -> bool:
    """
    returns a True if path is in exclusion list, taking recursivity into account.
    :param path:
    :param excluded_paths:
    :return:
    """
    path = str(path) if isinstance(path, Path) else path
    for e, r in excluded_paths.items():
        if (path.startswith(str(e)) and r) or path == e:
            return True
    return False


def get_recursive_file_list(path: (Path, str), excluded_paths) -> list:
    """
    returns a list of all files in path and subdirectory, minus excluded paths.
    :param path:
    :param excluded_paths:
    :return:
    """
    fl = []
    p = Path(path) if isinstance(path, str) else path
    for i in p.glob('**/*'):
        if i.is_file() and not is_excluded(str(i), excluded_paths):
            fl.append(i)
    return fl


def get_config_path() -> Path:
    """
    get config path , if possible by using XDG spec (?)
    :return: pathlib's Path object
    """
    droblo_config_folder = Path("~") / ".droblo"
    droblo_config_folder = droblo_config_folder.expanduser()
    if not droblo_config_folder.exists():
        droblo_config_folder.mkdir()
        logging.info(f"Created {droblo_config_folder}")
    return droblo_config_folder


def dump_connection_string(conn_string: str) -> bool:
    """
    dump connection string!
    :param conn_string:
    """

    try:
        (get_config_path() / "droblo.json").write_text(json.dumps(conn_string))
        return True
    except IOError:
        logging.exception("Failed to save connection string")
    return False


def load_connection_string() -> [str, None]:
    """
    load connection string!
    """

    try:
        conn_string_config = get_config_path() / "droblo.json"
        if conn_string_config.exists():
            with conn_string_config.open() as droblo_json:
                return json.load(droblo_json)
    except IOError:
        logging.error("Failed to load connection string")
    return None


def same_parent(src: (Path, str), dst: (Path, str)):
    """
    Test 2 paths and check if they have the same parent
    :param src:
    :param dst:
    :return:
    """
    src = Path(src) if isinstance(src, str) else src
    dst = Path(dst) if isinstance(dst, str) else dst
    return src.parent == dst.parent


def str_dict_to_path_dict(orm_dict: dict):
    """
    converts orm_dict keys from string to Path
    :param orm_dict:
    :return:
    """
    paths_dict = {}
    for p, r in orm_dict.items():
        paths_dict[Path(p).expanduser()] = r
    return paths_dict


def get_connection_string(main_args, obfuscated=False):
    """
    returns postgre connection string.
    :param obfuscated:
    :param main_args:
    :return:
    """
    conn_string = load_connection_string()
    if conn_string:
        if obfuscated:
            return re.sub(r'(postgresql://.*:).*(@.*)', r"\1password_is_obfucasted\2", conn_string)
        else:
            return conn_string
    elif main_args.db_password:
        if obfuscated:
            return "postgresql://%s:no_pwd_in_logs@%s:%s/%s" % (main_args.db_username,
                                                                main_args.db_host,
                                                                main_args.db_port,
                                                                main_args.db_name)
        else:
            return "postgresql://%s:%s@%s:%s/%s" % (main_args.db_username,
                                                    main_args.db_password,
                                                    main_args.db_host,
                                                    main_args.db_port,
                                                    main_args.db_name)
    else:
        logging.error("No password provided on the command line and config file not found.")
        sys.exit(1)


def logon_start_install_src_dst(root):
    """
    Returns src file and dst folder for logon startup setup, based on the OS.
    :return:
    """
    data = root / "data"
    if not data.exists():
        logging.critical("That's a bug.")
        sys.exit(-2)

    if sys.platform == 'linux':
        source_path = data / 'droblod.user.service'
        install_path = Path("~/.config/systemd/user/").expanduser()
    elif sys.platform == 'darwin':
        source_path = data / 'droblod.plist'
        install_path = Path("~/Library/LaunchAgents/").expanduser()
    elif sys.platform == 'win32':
        source_path = data / 'Droblod.xml'
        install_path = Path(r"C:\temp")
    else:
        source_path = None
        install_path = None
    return source_path, install_path


def logon_start_install(root):
    """
    Installs the logon start file (and creates the scheduled task under Windows.)
    """
    logging.info("Setting up logon start.")
    src, dst = logon_start_install_src_dst(root=root)
    if src and dst:
        if not dst.exists():
            logging.warning(f"Creating {dst}")
            dst.mkdir(parents=True)
        dst_file = dst / src.name
        if not dst_file.exists():
            dst_file.write_text(src.read_text())
            logging.info(f"{src} saved to {dst}")
            if sys.platform != 'darwin':
                import subprocess
                if sys.platform == "linux":
                    _cmd = ["systemctl", "--user", "--enable", "droblod.user"]
                else:
                    _cmd = ["schtasks.exe", "/create", "/XML", str(dst_file), "/tn", "droblod"]

                rtn = subprocess.run(_cmd, capture_output=True)
                if rtn.returncode == 0:
                    logging.info("Logon start successfully setup")
                else:
                    logging.warning("logon start setup failed")
                    logging.warning(rtn.stdout)
                    logging.warning(rtn.stderr)
        else:
            logging.warning(f"{dst_file} already exists.")
    else:
        logging.warning(f"logon_start for {sys.platform} is not implemented at the moment.")
