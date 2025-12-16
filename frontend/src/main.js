import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import { createRouter, createWebHistory } from 'vue-router'
import 'vuetify/styles'
import '@mdi/font/css/materialdesignicons.css'

// Clean up any existing service workers to prevent sw.js errors
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.getRegistrations().then(function(registrations) {
    for(let registration of registrations) {
      registration.unregister()
    }
  })
}

import App from './App.vue'
// Composants principaux depuis views
import Home from './views/Home.vue'
import About from './views/About.vue'
import Services from './views/Services.vue'
import Contact from './views/Contact.vue'
import Blog from './views/Blog.vue'
import Formations from './views/Formations.vue'
import Governance from './views/Gouvernance.vue'
// Composants secondaires depuis components
import Conference from './components/Conference.vue'
import Environment from './components/Environment.vue'
import Society from './components/Society.vue'
import News from './components/News.vue'
import Rewards from './components/Rewards.vue'
import Program from './components/Program.vue'
import Certification from './components/Certification.vue'
import Consulting from './components/Consulting.vue'
import Partner from './components/Partner.vue'
import Engagement from './components/Engagement.vue'
import PracticalInfo from './components/PracticalInfo.vue'
import Register from './components/Register.vue'
import AfterWork from './components/AfterWork.vue'
import WhyChoose from './components/WhyChoose.vue'
import Publications from './components/Publications.vue'
import Vision from './components/Vision.vue'

// ESG Colors based on graphic charter
const esgTheme = {
  dark: false,
  colors: {
    primary: '#2E7D32', // Environment Green
    secondary: '#FF6F00', // Social Orange  
    accent: '#C62828', // Governance Red
    info: '#546E7A', // Stratégies Grey
    warning: '#FF8F00',
    error: '#D32F2F',
    success: '#388E3C'
  }
}

const vuetify = createVuetify({
  theme: {
    defaultTheme: 'esgTheme',
    themes: {
      esgTheme
    }
  }
})

const routes = [
  // Pages principales (selon l'ordre du menu)
  { path: '/', component: Home, name: 'Accueil' },
  { path: '/qui-sommes-nous', component: About, name: 'Qui sommes-nous ?' },
  { path: '/africa-corporate-sustainability-conference', component: Conference, name: 'Africa Corporate Sustainability Conference' },
  { path: '/nos-services', component: Services, name: 'Nos Services' },
  { path: '/environnement-et-ressources-naturelles', component: Environment, name: 'Environnement et Ressources Naturelles' },
  { path: '/societe', component: Society, name: 'Société' },
  { path: '/a-propos', component: About, name: 'A Propos' },
  { path: '/news-articles', component: News, name: 'News & articles' },
  { path: '/recompenses', component: Rewards, name: 'Récompenses' },
  { path: '/programme', component: Program, name: 'Programme' },
  { path: '/contact', component: Contact, name: 'Contact' },
  
  // Autres pages
  { path: '/blog', component: Blog, name: 'Blog' },
  { path: '/certification-labelisation-notation-esg', component: Certification, name: 'Certification/Labélisation et Notation ESG' },
  { path: '/conseil-strategie-rse-dd', component: Consulting, name: 'Conseil en stratégie RSE/DD' },
  { path: '/devenez-partenaire', component: Partner, name: 'Devenez partenaire' },
  { path: '/engagement-politique-rse-dd', component: Engagement, name: 'Engagement/Politique RSE-DD' },
  { path: '/formations', component: Formations, name: 'Formations' },
  { path: '/gouvernance', component: Governance, name: 'Gouvernance' },
  { path: '/informations-pratique', component: PracticalInfo, name: 'Informations Pratique' },
  { path: '/inscrivez-vous', component: Register, name: 'Inscrivez vous' },
  { path: '/les-after-work-rse', component: AfterWork, name: 'Les After Work RSE' },
  { path: '/pourquoi-nous-choisir', component: WhyChoose, name: 'Pourquoi nous choisir ?' },
  { path: '/publications', component: Publications, name: 'Publications' },
  { path: '/vision-mission-valeurs', component: Vision, name: 'Vision Mission Valeurs' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

createApp(App)
  .use(vuetify)
  .use(router)
  .mount('#app')