// ==========================================
// MENÚ HAMBURGUESA
// ==========================================
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });
    }
    
    // Cerrar menú al hacer click en un enlace
    const navLinks = document.querySelectorAll('.nav-menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (hamburger) hamburger.classList.remove('active');
            if (navMenu) navMenu.classList.remove('active');
            document.body.style.overflow = '';
        });
    });
    
    // ==========================================
    // NAVBAR SCROLL EFFECT
    // ==========================================
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        if (currentScroll > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
    
    // ==========================================
    // ANIMACIONES AL HACER SCROLL
    // ==========================================
    const animateElements = document.querySelectorAll('.animate-on-scroll');
    
    if (animateElements.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });
        
        animateElements.forEach(element => {
            observer.observe(element);
        });
    }
    
    // ==========================================
    // CONTADOR DE CARACTERES PARA FORMULARIO
    // ==========================================
    const mensajeInput = document.querySelector('textarea[name="mensaje"]');
    if (mensajeInput) {
        const counter = document.createElement('small');
        counter.style.cssText = `
            display: block;
            text-align: right;
            color: #6B7A8F;
            font-size: 0.85rem;
            margin-top: 0.3rem;
        `;
        mensajeInput.parentNode.appendChild(counter);
        
        function updateCounter() {
            const length = mensajeInput.value.length;
            const max = mensajeInput.getAttribute('maxlength') || 500;
            counter.textContent = `${length} / ${max} caracteres`;
            
            if (length > max * 0.9) {
                counter.style.color = '#dc3545';
            } else {
                counter.style.color = '#6B7A8F';
            }
        }
        
        mensajeInput.addEventListener('input', updateCounter);
        updateCounter();
    }
    
    // ==========================================
    // BOTÓN DE VOLVER ARRIBA
    // ==========================================
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '↑';
    backToTop.style.cssText = `
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #0A2540 0%, #00B4D8 100%);
        color: white;
        border: none;
        font-size: 1.5rem;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(0, 180, 216, 0.3);
        transition: all 0.3s ease;
        opacity: 0;
        transform: translateY(20px);
        z-index: 999;
    `;
    document.body.appendChild(backToTop);
    
    backToTop.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTop.style.opacity = '1';
            backToTop.style.transform = 'translateY(0)';
        } else {
            backToTop.style.opacity = '0';
            backToTop.style.transform = 'translateY(20px)';
        }
    });
    
    console.log('🔒 NETLANWEB - Seguridad y Tecnología');
    console.log('🚀 Sitio web cargado correctamente');
});