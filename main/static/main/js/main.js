// Загрузка сайта
document.addEventListener('DOMContentLoaded', () => {
    document.body.style.opacity = "0";
    document.body.style.transition = "opacity 1s ease";

    setTimeout(() => {
        document.body.style.opacity = "1";
    }, 500);
});

// Плавная прокрутка к секции
function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}

// Анимация появления секций
document.addEventListener('DOMContentLoaded', () => {
    const sections = document.querySelectorAll('section');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    });

    sections.forEach(section => {
        section.classList.add('hidden');
        observer.observe(section);
    });
});

// Проверка полей логина
const loginForm = document.querySelector('form');
if (loginForm) {
    loginForm.addEventListener('submit', e => {
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        if (!username || !password) {
            e.preventDefault();
            showNotification('Please fill out all fields.');
        }
    });
}

// Всплывающее уведомление
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.classList.add('visible');
    }, 10);

    setTimeout(() => {
        notification.classList.remove('visible');
        setTimeout(() => notification.remove(), 300);
    }, 3000);
}

// Вызов уведомления при успешной загрузке страницы
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.search.includes('success=true')) {
        showNotification('Login successful!');
    }
});

// Административный код
const ADMIN_CODE = "55555";

document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');

    if (registerForm) {
        registerForm.addEventListener('submit', e => {
            const adminCodeInput = document.getElementById('admin-code').value.trim();

            if (adminCodeInput !== ADMIN_CODE) {
                e.preventDefault();
                showNotification('Invalid admin code. Only administrators can register new users.');
            }
        });
    }
});

// Плавная навигация по ссылкам (для прокрутки)
const links = document.querySelectorAll('a[href^="#"]');
links.forEach(link => {
    link.addEventListener('click', e => {
        e.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);

        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    });
});
// Скрытие загрузочного экрана после полной загрузки страницы
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const preloader = document.getElementById('preloader');
        preloader.classList.add('hidden');
    }, 1000); // 1-секундная задержка для плавного скрытия
});
