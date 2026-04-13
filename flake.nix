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
    {
      devShells.x86_64-linux.default =
        let
          pkgs = nixpkgs.legacyPackages.x86_64-linux;
        in
        pkgs.mkShell {
          packages = [
            vpython.packages.x86_64-linux.vpython
          ];
          shellHook = ''
            echo "vpython enabled"
            export PS1="\[\033[0;32m\]vpython-\e[38;5;141m\]\$\[\e[0m\]\[\033[0m\] "
          '';
        };
    };
}
