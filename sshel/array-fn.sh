function downloadPatches {
  patch_apply_order=("${!1}")
  for aPatch in ${patch_apply_order[@]}; do
    echo "Downloading patch: ${aPatch}"
  done
}


patch_apply_order=(p26045997_122130_Generic.zip p26626168_122130_Generic.zip p27010571_122130_Generic.zip)
downloadPatches patch_apply_order[@]
