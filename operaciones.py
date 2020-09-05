#operaciones
a=3;b=5;c=4;d=3;
af=2.5;bf=3.24;cf=6.32;df=1.54;
#suma;
suma=a+d;
print(f'la suma entre a y d es\n>>{a}+{d} = {suma}\nambos son int, el resultado es un int');
#resta
resta=bf-df;
print(f'la resta entre bf y df es\n>>{bf}-{df} = {resta}\naf es un float mientras b es un int, el resultado es un float');
#division
division=c/df;
print(f'la division entre c y df es\n>>{c}/{df}={division}\nArroja todos los valores correspondientes y el resultado es un float \nEn caso de ser division entera:\n>>{c}//{df} = {c//df}\nEl resultado sigue siendo un float');
#multiplicacion
multiplicacion=d*cf;
print(f'la multiplicacion entre d y cf es\n>>{d}*{cf} = {multiplicacion}');
#modulo
modulo=a%bf;
print(f'el modulo entre a y bf es\n>>{a}%{bf} = {modulo}');
