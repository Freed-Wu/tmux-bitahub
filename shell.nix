{ pkgs ? import <nixpkgs> { } }:

with pkgs;
mkShell {
  name = "tmux-bitahub";
  buildInputs = [
    (python3.withPackages (
      p: with p; [
        beautifulsoup4
        lxml
        pandas
      ]
    ))
  ];
}
