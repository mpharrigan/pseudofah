module load amber/14-cuda

{% if gen == 0 -%}
pmemd.cuda -i mdin.{{gen}} -o mdout.{{gen}} -p prmtop -c inpcrd -r restrt -x mdcrd.{{gen}} -inf mdinfo
{% else %}
pmemd.cuda -O -i mdin.{{gen}} -o mdout.{{gen}} -p prmtop -c restrt -r restrt -x mdcrd.{{gen}} -inf mdinfo
{% endif %}
