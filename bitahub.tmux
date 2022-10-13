#!/usr/bin/env bash
# shellcheck disable=SC2155
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

interpolation=(
  "\#{bitahub_status_titanxp}"
  "\#{bitahub_status_gtx1080ti}"
  "\#{bitahub_status_rtx3090}"
  "\#{bitahub_status_teslav100}"
  "\#{bitahub_status_debug}"
)
commands=(
  "#($CURRENT_DIR/scripts/bitahub.py titanxp)"
  "#($CURRENT_DIR/scripts/bitahub.py gtx1080ti)"
  "#($CURRENT_DIR/scripts/bitahub.py rtx3090)"
  "#($CURRENT_DIR/scripts/bitahub.py teslav100)"
  "#($CURRENT_DIR/scripts/bitahub.py debug)"
)

get_tmux_option() {
  local option=$1
  local default_value=$2
  local option_value=$(tmux show-option -gqv "$option")
  if [ -z "$option_value" ]; then
    echo "$default_value"
  else
    echo "$option_value"
  fi
}

set_tmux_option() {
  local option="$1"
  local value="$2"
  tmux set-option -gq "$option" "$value"
}

do_interpolation() {
  local all_interpolated="$1"
  for ((i = 0; i < ${#commands[@]}; i++)); do
    all_interpolated=${all_interpolated//${interpolation[$i]}/${commands[$i]}}
  done
  echo "$all_interpolated"
}

update_tmux_option() {
  local option="$1"
  local option_value="$(get_tmux_option "$option")"
  local new_option_value="$(do_interpolation "$option_value")"
  set_tmux_option "$option" "$new_option_value"
}

main() {
  update_tmux_option "status-right"
  update_tmux_option "status-left"
}
main
