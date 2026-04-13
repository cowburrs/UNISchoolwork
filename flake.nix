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
        };
    };
}
