# shell.nix
let
  pkgs = import <nixpkgs> {};
  python = pkgs.python3;

  vpython = python.pkgs.buildPythonPackage rec {
    pname = "vpython";
    version = "7.6.5";
    format = "wheel";  # use the prebuilt wheel to avoid Cython build issues

    src = python.pkgs.fetchPypi {
      inherit pname version;
      # grab the manylinux wheel for your python version
      format = "wheel";
      dist = "cp312";
      python = "cp312";
      abi = "cp312";
      platform = "manylinux_2_17_x86_64.manylinux2014_x86_64";
      sha256 = ""; # fill in with `nix-prefetch-url <wheel url>`
    };

    propagatedBuildInputs = with python.pkgs; [
      jupyterlab
      ipywidgets
      requests
      pygments
    ];
  };

in pkgs.mkShell {
  packages = [ (python.withPackages (ps: [ vpython ])) ];
}
