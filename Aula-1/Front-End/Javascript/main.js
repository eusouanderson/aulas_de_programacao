// Seleciona o botão pelo seu ID
const welcomeButton = document.getElementById('welcomeButton');

// Adiciona um evento de clique ao botão
welcomeButton.addEventListener('click', function() {
    // Exibe uma mensagem de alerta quando o botão é clicado
    alert('Bem-vindo ao meu site! Aproveite a navegação.');
});

// Função para verificar se um elemento está visível na tela
function isElementInViewport(element) {
    const rect = element.getBoundingClientRect(); // Obtém as dimensões e a posição do elemento
    return (
        rect.top >= 0 && // A parte superior do elemento está visível na tela
        rect.left >= 0 && // A parte esquerda do elemento está visível na tela
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) && // A parte inferior do elemento está visível na tela
        rect.right <= (window.innerWidth || document.documentElement.clientWidth) // A parte direita do elemento está visível na tela
    );
}

// Função para adicionar a classe 'active' quando as seções entram na visualização
function animateSections() {
    const sections = document.querySelectorAll('.animated-section'); // Seleciona todas as seções animadas
    sections.forEach(section => {
        if (isElementInViewport(section)) { // Verifica se a seção está visível
            section.classList.add('active'); // Adiciona a classe 'active' para animar a seção
        }
    });
}

// Chama a função de animação na rolagem e ao carregar a página
window.addEventListener('scroll', animateSections); // Adiciona evento de rolagem
window.addEventListener('load', animateSections); // Adiciona evento de carregamento da página

