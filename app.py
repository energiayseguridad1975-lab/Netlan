from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, TextAreaField, SubmitField, TelField
from wtforms.validators import DataRequired, Email, Length
from datetime import datetime

# ============================================
# CONFIGURACIÓN DE LA APLICACIÓN
# ============================================
app = Flask(__name__)
app.secret_key = 'netlan-seguridad-monterrey-2024'

# ============================================
# FORMULARIO DE CONTACTO
# ============================================
class ContactForm(FlaskForm):
    nombre = StringField('Nombre completo', validators=[
        DataRequired(message='El nombre es obligatorio'),
        Length(min=2, max=100)
    ])
    email = EmailField('Correo electrónico', validators=[
        DataRequired(message='El email es obligatorio'),
        Email(message='Ingresa un email válido')
    ])
    telefono = TelField('Teléfono', validators=[
        DataRequired(message='El teléfono es obligatorio'),
        Length(min=10, max=15)
    ])
    mensaje = TextAreaField('Mensaje', validators=[
        DataRequired(message='El mensaje es obligatorio'),
        Length(min=10, max=500)
    ])
    enviar = SubmitField('Solicitar Información')

# ============================================
# RUTAS
# ============================================

@app.route('/')
def index():
    return render_template('index.html', 
                         titulo="Inicio",
                         year=datetime.now().year)

@app.route('/servicios')
def servicios():
    servicios_lista = [
        {
            'nombre': 'Cámaras de Seguridad', 
            'descripcion': 'Sistemas de videovigilancia de última generación para monitoreo en tiempo real, con acceso remoto desde cualquier dispositivo.', 
            'icono': '📹',
            'detalles': 'Cámaras IP, Analógicas, NVR, DVR, Visión Nocturna'
        },
        {
            'nombre': 'Control de Accesos', 
            'descripcion': 'Soluciones inteligentes para gestionar y controlar el acceso a tus instalaciones, con tecnología biométrica y RFID.', 
            'icono': '🚪',
            'detalles': 'Biometría, Tarjetas RFID, Lectores de Huella, Torniquetes'
        },
        {
            'nombre': 'Automatización', 
            'descripcion': 'Automatiza procesos y sistemas en tu empresa para mejorar la eficiencia y reducir costos operativos.', 
            'icono': '⚙️',
            'detalles': 'Domótica, Control de Iluminación, Sensores IoT'
        },
        {
            'nombre': 'Monitoreo Remoto', 
            'descripcion': 'Accede a tus sistemas de seguridad desde cualquier lugar del mundo a través de nuestra plataforma en la nube.', 
            'icono': '📡',
            'detalles': 'Acceso 24/7, App Móvil, Alertas en Tiempo Real'
        },
        {
            'nombre': 'Instalación Profesional', 
            'descripcion': 'Instalación y configuración de todos tus sistemas de seguridad con los más altos estándares de calidad.', 
            'icono': '🔧',
            'detalles': 'Instalación Certificada, Cableado Estructurado'
        },
        {
            'nombre': 'Mantenimiento', 
            'descripcion': 'Planes de mantenimiento preventivo y correctivo para asegurar el óptimo funcionamiento de tus equipos.', 
            'icono': '🛠️',
            'detalles': 'Mantenimiento Preventivo, Correctivo, Soporte 24/7'
        }
    ]
    return render_template('servicios.html', 
                         servicios=servicios_lista,
                         titulo="Servicios",
                         year=datetime.now().year)

@app.route('/portafolio')
def portafolio():
    proyectos = [
        {
            'titulo': 'Torre Corporativa', 
            'categoria': 'Seguridad', 
            'imagen': '🏢',
            'descripcion': 'Sistema de videovigilancia y control de accesos para edificio de 20 pisos con más de 100 cámaras.',
            'cliente': 'Torre Insignia'
        },
        {
            'titulo': 'Planta Industrial', 
            'categoria': 'Automatización', 
            'imagen': '🏭',
            'descripcion': 'Automatización de puertas de acceso y sistemas de seguridad perimetral en planta de 50,000 m².',
            'cliente': 'Industrias Monterrey'
        },
        {
            'titulo': 'Centro Comercial', 
            'categoria': 'Monitoreo', 
            'imagen': '🛍️',
            'descripcion': 'Monitoreo de 150 cámaras con análisis de video inteligente para centro comercial de 3 niveles.',
            'cliente': 'Plaza Real'
        },
        {
            'titulo': 'Residencia Privada', 
            'categoria': 'Domótica', 
            'imagen': '🏠',
            'descripcion': 'Sistema completo de seguridad y automatización para hogar inteligente con control por voz.',
            'cliente': 'Residencial Las Palmas'
        }
    ]
    return render_template('portafolio.html', 
                         proyectos=proyectos,
                         titulo="Portafolio",
                         year=datetime.now().year)

@app.route('/nosotros')
def nosotros():
    equipo = [
        {'nombre': 'Ing. Carlos Rodríguez', 'cargo': 'Director General', 'avatar': '👨‍💼'},
        {'nombre': 'Ing. Ana Martínez', 'cargo': 'Jefa de Operaciones', 'avatar': '👩‍💼'},
        {'nombre': 'Ing. Miguel Torres', 'cargo': 'Especialista en Seguridad', 'avatar': '👨‍🔧'},
        {'nombre': 'Lic. Laura Garza', 'cargo': 'Atención a Clientes', 'avatar': '👩‍💻'},
        {'nombre': 'Ing. Roberto Sánchez', 'cargo': 'Soporte Técnico', 'avatar': '👨‍🏫'},
        {'nombre': 'Lic. Patricia López', 'cargo': 'Ventas', 'avatar': '👩‍💼'}
    ]
    return render_template('nosotros.html', 
                         equipo=equipo,
                         titulo="Nosotros",
                         year=datetime.now().year)

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    if form.validate_on_submit():
        flash('¡Mensaje enviado con éxito! Un asesor se pondrá en contacto contigo en las próximas 24 horas.', 'success')
        return redirect(url_for('contacto'))
    return render_template('contacto.html', 
                         form=form,
                         titulo="Contacto",
                         year=datetime.now().year)

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html', titulo="Error 404"), 404

@app.errorhandler(500)
def error_servidor(error):
    return render_template('500.html', titulo="Error 500"), 500

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 INICIANDO NETLANWEB - Seguridad y Tecnología")
    print("=" * 60)
    print("📍 Servidor local: http://localhost:5000")
    print("📧 Email: dlopez@netlanweb.com")
    print("📱 Teléfono: 81 1082 8156")
    print("💡 Presiona CTRL+C para detener")
    print("=" * 60)
    app.run(debug=True, host='0.0.0.0', port=5000)