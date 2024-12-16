// Плавная прокрутка
document.addEventListener('DOMContentLoaded', () => {
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
});

// Проверка полей логина
const loginForm = document.querySelector('form');
if (loginForm) {
    loginForm.addEventListener('submit', e => {
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        if (!username || !password) {
            e.preventDefault();
            alert('Please fill out all fields.');
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

// Вызов уведомления
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.search.includes('success=true')) {
        showNotification('Login successful!');
    }
});

// Административный код
const ADMIN_CODE = "55555"; // Замените на свой уникальный код

document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');
    
    if (registerForm) {
        registerForm.addEventListener('submit', (e) => {
            const adminCodeInput = document.getElementById('admin-code').value.trim();

            if (adminCodeInput !== ADMIN_CODE) {
                e.preventDefault();
                alert('Invalid admin code. Only administrators can register new users.');
            }
        });
    }
});
