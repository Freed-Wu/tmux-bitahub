{ pkgs ? import <nixpkgs> { } }:

with pkgs;
mkShell {
  name = "tmux-bitahub";
  buildInputs = [
    tmux

    (python3.withPackages (
      p: with p; [
        beautifulsoup4
        lxml
        pandas
      ]
    ))
  ];
}
