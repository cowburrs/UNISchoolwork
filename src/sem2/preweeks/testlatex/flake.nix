{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    {
      nixpkgs,
      ...
    }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in
    {

      packages.x86_64-linux.default = pkgs.stdenv.mkDerivation {
        name = "latex";
        src = ./.;
        buildInputs = [
          (pkgs.texlive.combine {
            inherit (pkgs.texlive)
              scheme-basic
              biber
              biblatex
              ;
          })
        ]
        ++ (with pkgs; [
          pandoc
        ]);
        buildPhase = ''
          runHook preBuild
          pdflatex ./Main.tex
          biber main
          pdflatex ./Main.tex
          pandoc ./Main.tex -o ./Main.epub
          runHook postBuild
        '';
        installPhase = ''
          runHook preInstall
          mkdir -p $out/pdf/
          cp -r ./Main.pdf $out/pdf/
          mkdir -p $out/epub/
          cp -r ./Main.epub $out/epub/
          runHook postInstall
        '';
      };

      devShells.x86_64-linux.default = pkgs.mkShell {
        shellHook = ''
          nix develop ../.#
          exit
        '';
      };
    };
}
