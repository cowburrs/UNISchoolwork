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
      devShells.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
        packages = [
          vpython.packages.x86_64-linux.vpython
        ];
        shellHook = ''
          export PS1="\n\[\033[1;32m\][nix-shell:\w]\$\[\033[0m\] "
        '';
      };
    };
}
