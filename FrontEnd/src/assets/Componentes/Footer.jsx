import React from 'react';
import footer_azul from "../Imgs/FooterAdmin.png";
import footer_verde from "../Imgs/FooterGestor.png";
import footer_ciano from "../Imgs/FooterIns.png";

function Footer({ azul, azul_aprendiz, verde, ciano, home }) {
    // Verifica se todas as propriedades são falsas
    if (!azul && !azul_aprendiz && !verde && !ciano && !home) {
        // Se todas forem falsas, não renderiza o footer
        return null;
    }

    // Adiciona classes CSS com base nas propriedades recebidas
    let className = "";
    if (azul || azul_aprendiz || home) {
        className = "azul";
    } else if (verde) {
        className = "verde";
    } else if (ciano) {
        className = "ciano";
    }

    // Renderiza a imagem de acordo com a classe CSS
    return (
        <img src={getClassImage(className)} className={`w-full ${className}`} alt="Footer" />
    );
}

// Retorna a imagem correspondente com base na classe CSS
function getClassImage(className) {
    switch (className) {
        case 'azul':
            return footer_azul;
        case 'verde':
            return footer_verde;
        case 'ciano':
            return footer_ciano;
        default:
            return "";
    }
}

export default Footer;
