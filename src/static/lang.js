const translations = {
  en: {
    title: "Welcome",
    heading: "Welcome to my website",
    paragraph: "This is a multilingual example."
  },
  es: {
    title: "Bienvenido",
    heading: "Bienvenido a mi sitio web",
    paragraph: "Este es un ejemplo multilingüe."
  },
  fr: {
    title: "Bienvenue",
    heading: "Bienvenue sur mon site web",
    paragraph: "Ceci est un exemple multilingue."
  }
};

const switchLanguage = (lang) => {
  document.querySelectorAll('[data-i18n]').forEach(elem => {
    const key = elem.getAttribute('data-i18n');
    if (translations[lang][key]) {
      elem.innerText = translations[lang][key];
    }
  });
};

// Default language
document.getElementById('languageSwitcher').addEventListener('change', (e) => {
  switchLanguage(e.target.value);
});

// Set initial language
switchLanguage('en');
