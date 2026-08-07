{
  description = "Nixos dev environment for my schoolwork";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    pyproject-nix = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    uv2nix = {
      url = "github:pyproject-nix/uv2nix";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
    pyproject-build-systems = {
      url = "github:pyproject-nix/build-system-pkgs";
      inputs.pyproject-nix.follows = "pyproject-nix";
      inputs.uv2nix.follows = "uv2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
  outputs =
    {
      nixpkgs,
      pyproject-nix,
      uv2nix,
      pyproject-build-systems,
      ...
    }:
    let
      inherit (nixpkgs) lib;
      system = "x86_64-linux";
      workspace = uv2nix.lib.workspace.loadWorkspace { workspaceRoot = ./.; };
      overlay = workspace.mkPyprojectOverlay {
        sourcePreference = "wheel";
      };
      editableOverlay = workspace.mkEditablePyprojectOverlay {
        root = "$REPO_ROOT";
      };
      pythonSets =
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.python3;
        in
        (pkgs.callPackage pyproject-nix.build.packages {
          inherit python;
        }).overrideScope
          (
            lib.composeManyExtensions [
              pyproject-build-systems.overlays.wheel
              overlay
              (
                final: _prev:
                let
                  inherit (final) pkgs;
                  hacks = pkgs.callPackage pyproject-nix.build.hacks { };
                in
                {
                  tkinter = hacks.nixpkgsPrebuilt {
                    from = python.pkgs.tkinter;
                  };
                }
              )
            ]
          );
      pkgs = nixpkgs.legacyPackages.${system};
      myPythonPackages =
        ps: with ps; [
          numpy
          matplotlib
          pandas
          schemdraw
          uncertainties
          scipy
        ];
      patchedQuarto =
        (pkgs.quarto.override {
          extraPythonPackages = myPythonPackages;
        }).overrideAttrs
          (oldAttrs: {
            postPatch = (oldAttrs.postPatch or "") + ''
              substituteInPlace bin/quarto.js \
                --replace-fail "syntax-highlighting" "highlight-style"
            '';
          });
    in
    rec {

      packages.x86_64-linux.mkbib = pkgs.writeShellApplication {
        name = "mkbib";
        runtimeInputs = with pkgs; [
          (python3.withPackages (p: [
            p.pyzotero
          ]))
          jq
        ];
        text = ''
          b=$(jq -r '.password_name' pytero.json)
          a=$(bw get password "$b")
          python ${./ci/mkbib.py} "$a"
        '';
      };
      packages.x86_64-linux.getkeys = pkgs.writeShellApplication {
        name = "getkeys";
        runtimeInputs = with pkgs; [
          (python3.withPackages (p: [
            p.pyzotero
          ]))
          jq
        ];
        text = ''
          b=$(jq -r '.password_name' pytero.json)
          a=$(bw get password "$b")
          python ${./ci/getkeys.py} "$a"
        '';
      };

      devShells.${system} =
        let
          pythonSet = pythonSets.overrideScope editableOverlay;
          # virtualenv = pythonSet.mkVirtualEnv "hello-world-dev-env" workspace.deps.all;
          virtualenv = pythonSet.mkVirtualEnv "hello-tkinter-dev-env" (
            workspace.deps.all
            // {
              tkinter = [ ];
            }
          );
        in
        {
          PHYS1201 = pkgs.mkShell {
            packages = [
              patchedQuarto
            ]
            ++ (with pkgs; [
              isort
              black
              texliveFull
              pyright
              librsvg
              entr
              nsxiv
              (python3.withPackages myPythonPackages)
            ]);
            shellHook = ''
              export REPO_ROOT=$(git rev-parse --show-toplevel)
              export PS1="\n\[\033[1;32m\][nix-shell:\w]\$\[\033[0m\] "
            '';
          };
          ENGN1218 = pkgs.mkShell {
            packages = [
            ]
            ++ (with pkgs; [
              isort
              black
              pyright
              (python3.withPackages (
                ps: with ps; [
                  sympy
                ]
              ))
              entr
            ]);
            shellHook = ''
              export REPO_ROOT=$(git rev-parse --show-toplevel)
              export PS1="\n\[\033[1;32m\][nix-shell:\w]\$\[\033[0m\] "
            '';
          };
          ENGN1217 = pkgs.mkShell {
            packages = [
            ]
            ++ (with pkgs; [
              isort
              black
              pyright
              (python3.withPackages (
                ps: with ps; [
                  numpy
                  sympy
                ]
              ))
              entr
            ]);
            shellHook = ''
              export REPO_ROOT=$(git rev-parse --show-toplevel)
              export PS1="\n\[\033[1;32m\][nix-shell:\w]\$\[\033[0m\] "
            '';
          };
          default = pkgs.mkShell {
            packages = [
              packages.x86_64-linux.getkeys
              packages.x86_64-linux.mkbib
              virtualenv
              pkgs.uv
              patchedQuarto
            ]
            ++ (with pkgs; [
              isort
              black
              pyright
              # ghc
              # haskell-language-server
              # ormolu
              octave
              # (with haskellPackages; [
              #   doctest
              # ])
              graphviz
              (with python314Packages; [
                miss-hit
              ])
              matlab-language-server
              texlab
              tex-fmt
            ]);
            env = {
              UV_NO_SYNC = "1";
              UV_PYTHON = pythonSet.python.interpreter;
              UV_PYTHON_DOWNLOADS = "never";
            };
            shellHook = ''
              unset PYTHONPATH
              export REPO_ROOT=$(git rev-parse --show-toplevel)
              export PS1="\n\[\033[1;32m\][nix-shell:\w]\$\[\033[0m\] "
            '';
          };
        };

    };
}
