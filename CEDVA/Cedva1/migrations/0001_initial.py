# Generated by Django 4.1.1 on 2022-10-11 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idalumno', models.BigAutoField(primary_key=True, serialize=False)),
                ('matricula', models.CharField(blank=True, max_length=100)),
                ('nombreA', models.CharField(max_length=100)),
                ('apellidoPA', models.CharField(max_length=100)),
                ('apellidoMA', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('convenio', models.CharField(max_length=800)),
                ('inicioCurso', models.DateField()),
                ('finalCurso', models.DateField()),
                ('observaciones', models.CharField(max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'alumno',
                'verbose_name_plural': 'alumnos',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('iddireccion', models.BigAutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=100)),
                ('lote', models.IntegerField()),
                ('manzana', models.IntegerField()),
                ('colonia', models.CharField(max_length=100)),
                ('delegacionMunicipio', models.CharField(max_length=100)),
                ('codigopostal', models.IntegerField()),
                ('ciudadOestado', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'direccion',
                'verbose_name_plural': 'direcciones',
            },
        ),
        migrations.CreateModel(
            name='Escuela',
            fields=[
                ('idescuela', models.BigAutoField(primary_key=True, serialize=False)),
                ('plantel', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'plantel',
                'verbose_name_plural': 'planteles',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('idtutor', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreT', models.CharField(max_length=100)),
                ('apellidoPT', models.CharField(max_length=100)),
                ('apellidoMT', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('padreT', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'tutor',
                'verbose_name_plural': 'tutores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('tipo', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idpago', models.BigAutoField(primary_key=True, serialize=False)),
                ('folio', models.IntegerField()),
                ('tipoPago', models.CharField(max_length=100)),
                ('monto', models.IntegerField()),
                ('fechaPago', models.DateField()),
                ('mesPagado', models.CharField(max_length=12)),
                ('horapago', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('idalumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories7', to='Cedva1.alumno')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('idespecialidad', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombreE', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('idescuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories8', to='Cedva1.escuela')),
            ],
            options={
                'verbose_name': 'especialidad',
                'verbose_name_plural': 'especialidades',
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='iddireccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories2', to='Cedva1.direccion'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='idescuela',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='Cedva1.escuela'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='idespecialidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories1', to='Cedva1.especialidad'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='idtutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories3', to='Cedva1.tutor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='idusuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories4', to='Cedva1.usuario'),
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('idadministrador', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoP', models.CharField(max_length=100)),
                ('apellidoM', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('idescuela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories5', to='Cedva1.escuela')),
                ('idusuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories6', to='Cedva1.usuario')),
            ],
            options={
                'verbose_name': 'administrador',
                'verbose_name_plural': 'administradores',
            },
        ),
    ]