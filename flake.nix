{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    vpython.url = "github:Cowboylaserkittenjetshark/vpython-nix";
  };

  outputs =
    {
      nixpkgs,
      vpython,
      ...
    }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in
    {
      devShells.x86_64-linux.default = pkgs.mkShell {
        packages = [
          vpython.packages.x86_64-linux.vpython

          (pkgs.python3.withPackages (
            python-pkgs: with python-pkgs; [
              pyserial
              holidays
              pyqt6
              uncertainties
              pint
              pandas
              matplotlib
              numpy
              odfpy
            ]
          ))
        ];
        shellHook = ''
          export PS1="\n\[\033[1;32m\][nix-shell:\w]\$\[\033[0m\] "
        '';
      };
    };
}
