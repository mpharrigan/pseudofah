module load amber/14-cuda

{% if gen == 0 -%}
pmemd.cuda -i mdin.{{gen}} -o mdout.{{gen}} -p prmtop -c inpcrd -r restrt.{{gen}} -x mdcrd.{{gen}} -inf mdinfo.{{gen}}
{% else %}
pmemd.cuda -i mdin.{{gen}} -o mdout.{{gen}} -p prmtop -c restrt.{{gen-1}} -r restrt.{{gen}} -x mdcrd.{{gen}} -inf mdinfo.{{gen}}
{% endif %}
