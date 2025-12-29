<template>
  <v-app>
    <!-- Navigation Header -->
    <v-app-bar app color="white" elevation="2" height="80" class="mega-menu-header">
      <v-container fluid class="d-flex align-center">
        <!-- Logo -->
        <router-link to="/" class="d-flex align-center text-decoration-none logo-container">
          <v-img
            src="/logo_esg_blanc.jpg"
            alt="ESG Stratégies"
            height="50"
            width="auto"
            max-width="180"
            contain
            class="logo-img"
          />
        </router-link>

        <v-spacer />

        <!-- Desktop Mega Menu -->
        <div class="d-none d-lg-flex mega-menu-container">
          <!-- Accueil -->
          <v-btn
            to="/"
            variant="text"
            class="mx-1 nav-item"
            :color="$route.path === '/' ? 'primary' : 'grey-darken-1'"
          >
            Accueil
          </v-btn>

          <!-- Qui sommes-nous (Mega Menu) -->
          <v-menu offset-y content-class="mega-menu-content">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                variant="text"
                class="mx-1 nav-item"
                color="grey-darken-1"
              >
                Qui sommes-nous
                <v-icon size="small" class="ml-1">mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-card class="mega-menu-card" min-width="800">
              <v-card-text class="pa-6">
                <v-row>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="blue" class="mb-3">mdi-information</v-icon>
                      <h3 class="text-h6 mb-2">Présentation</h3>
                      <p class="text-body-2 mb-3">Découvrez notre histoire et notre expertise</p>
                      <v-btn to="/qui-sommes-nous" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="orange" class="mb-3">mdi-target</v-icon>
                      <h3 class="text-h6 mb-2">Vision & Mission</h3>
                      <p class="text-body-2 mb-3">Nos objectifs et valeurs fondamentales</p>
                      <v-btn to="/vision-mission-valeurs" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="purple" class="mb-3">mdi-handshake</v-icon>
                      <h3 class="text-h6 mb-2">Engagements</h3>
                      <p class="text-body-2 mb-3">Politique RSE et durabilité</p>
                      <v-btn to="/engagement-politique-rse-dd" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-menu>

          <!-- Services (Mega Menu) -->
          <v-menu offset-y content-class="mega-menu-content">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                variant="text"
                class="mx-1 nav-item"
                color="grey-darken-1"
              >
                Services
                <v-icon size="small" class="ml-1">mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-card class="mega-menu-card" min-width="1000">
              <v-card-text class="pa-6">
                <!-- Première ligne - 4 services -->
                <v-row class="mb-4">
                  <v-col cols="3" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="primary" class="mb-3">mdi-strategy</v-icon>
                      <h3 class="text-h6 mb-2">Stratégies ESG/RSE</h3>
                      <p class="text-body-2 mb-3">Élaboration de stratégies durables</p>
                      <v-btn to="/strategie-esg-rse" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="3" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="green" class="mb-3">mdi-earth</v-icon>
                      <h3 class="text-h6 mb-2">Évaluations Environnementales</h3>
                      <p class="text-body-2 mb-3">Analyse d'impact environnemental</p>
                      <v-btn to="/evaluation-environnementale" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="3" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="teal" class="mb-3">mdi-recycle</v-icon>
                      <h3 class="text-h6 mb-2">Économie circulaire</h3>
                      <p class="text-body-2 mb-3">Optimisation des ressources</p>
                      <v-btn to="/economie-circulaire" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="3" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="blue" class="mb-3">mdi-cloud-outline</v-icon>
                      <h3 class="text-h6 mb-2">Neutralité carbone</h3>
                      <p class="text-body-2 mb-3">Stratégies de décarbonation</p>
                      <v-btn to="/neutralite-carbone" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
                <!-- Deuxième ligne - 2 services -->
                <v-row>
                  <v-col cols="6" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="light-green" class="mb-3">mdi-leaf</v-icon>
                      <h3 class="text-h6 mb-2">Biodiversité et écosystèmes</h3>
                      <p class="text-body-2 mb-3">Protection de la biodiversité</p>
                      <v-btn to="/biodiversite-ecosystemes" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="6" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="indigo" class="mb-3">mdi-file-document-outline</v-icon>
                      <h3 class="text-h6 mb-2">Reporting durabilité ESG</h3>
                      <p class="text-body-2 mb-3">Rapports de durabilité</p>
                      <v-btn to="/reporting-durabilite-esg" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-menu>

          <!-- Notations ESG (Mega Menu) -->
          <v-menu offset-y content-class="mega-menu-content">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                variant="text"
                class="mx-1 nav-item"
                color="grey-darken-1"
              >
                Notations ESG
                <v-icon size="small" class="ml-1">mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-card class="mega-menu-card" min-width="600">
              <v-card-text class="pa-6">
                <v-row>
                  <v-col cols="4" class="text-center">
                      <div class="mega-menu-item">
                        <v-icon size="48" color="green" class="mb-3">mdi-star</v-icon>
                        <h3 class="text-h6 mb-2">Notation</h3>
                        <p class="text-body-2 mb-3">Évaluation et notation ESG des entreprises</p>
                        <v-btn to="/notation-rating" variant="outlined" size="small">
                          En savoir plus
                        </v-btn>
                      </div>
                    </v-col>
                  <v-col cols="4" class="text-center">
                      <div class="mega-menu-item">
                        <v-icon size="48" color="blue" class="mb-3">mdi-certificate</v-icon>
                        <h3 class="text-h6 mb-2">Labellisation</h3>
                        <p class="text-body-2 mb-3">Certification et labellisation ESG</p>
                        <v-btn to="/labelisation" variant="outlined" size="small">
                          En savoir plus
                        </v-btn>
                      </div>
                    </v-col>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="purple" class="mb-3">mdi-trophy</v-icon>
                      <h3 class="text-h6 mb-2">Classement</h3>
                      <p class="text-body-2 mb-3">Classement et benchmarking ESG</p>
                      <v-btn to="/classement" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-menu>

          <!-- Formations -->
          <v-btn
            to="/formations"
            variant="text"
            class="mx-1 nav-item"
            :color="$route.path === '/formations' ? 'primary' : 'grey-darken-1'"
          >
            Formations
          </v-btn>

          <!-- Événements (Mega Menu) -->
          <v-menu offset-y content-class="mega-menu-content">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                variant="text"
                class="mx-1 nav-item"
                color="grey-darken-1"
              >
                Événements
                <v-icon size="small" class="ml-1">mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-card class="mega-menu-card" min-width="800">
              <v-card-text class="pa-6">
                <v-row>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="indigo" class="mb-3">mdi-presentation</v-icon>
                      <h3 class="text-h6 mb-2">Conférences</h3>
                      <p class="text-body-2 mb-3">Africa Corporate Sustainability Conference</p>
                      <v-btn to="/africa-corporate-sustainability-conference" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="orange" class="mb-3">mdi-glass-cocktail</v-icon>
                      <h3 class="text-h6 mb-2">Afterwork RSE</h3>
                      <p class="text-body-2 mb-3">Rencontres networking et échanges</p>
                      <v-btn to="/les-after-work-rse" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="amber" class="mb-3">mdi-trophy</v-icon>
                      <h3 class="text-h6 mb-2">Récompenses</h3>
                      <p class="text-body-2 mb-3">Prix et reconnaissances ESG</p>
                      <v-btn to="/recompenses" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-menu>

          <!-- Ressources (Mega Menu) -->
          <v-menu offset-y content-class="mega-menu-content">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                variant="text"
                class="mx-1 nav-item"
                color="grey-darken-1"
              >
                Ressources
                <v-icon size="small" class="ml-1">mdi-chevron-down</v-icon>
              </v-btn>
            </template>
            <v-card class="mega-menu-card" min-width="800">
              <v-card-text class="pa-6">
                <v-row>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="deep-purple" class="mb-3">mdi-book-open</v-icon>
                      <h3 class="text-h6 mb-2">Publications</h3>
                      <p class="text-body-2 mb-3">Rapports, guides et études ESG</p>
                      <v-btn to="/publications" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="cyan" class="mb-3">mdi-newspaper</v-icon>
                      <h3 class="text-h6 mb-2">News & Articles</h3>
                      <p class="text-body-2 mb-3">Actualités et analyses du secteur</p>
                      <v-btn to="/news-articles" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="4" class="text-center">
                    <div class="mega-menu-item">
                      <v-icon size="48" color="pink" class="mb-3">mdi-post</v-icon>
                      <h3 class="text-h6 mb-2">Blog</h3>
                      <p class="text-body-2 mb-3">Réflexions et conseils d'experts</p>
                      <v-btn to="/blog" variant="outlined" size="small">
                        En savoir plus
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-menu>

          <!-- Contact -->
          <v-btn
            to="/contact"
            variant="text"
            class="mx-1 nav-item"
            :color="$route.path === '/contact' ? 'primary' : 'grey-darken-1'"
          >
            Contact
          </v-btn>
        </div>

        <!-- Search Button -->
        <v-btn
          icon
          @click="searchDialog = true"
          class="ml-2"
        >
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <!-- Mobile Menu Button -->
        <v-btn
          icon
          @click="drawer = true"
          class="d-lg-none ml-2"
        >
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </v-container>
    </v-app-bar>

    <!-- Mobile Navigation Drawer -->
    <v-navigation-drawer
      v-model="drawer"
      temporary
      location="right"
      width="300"
    >
      <v-list>
        <v-list-item
          prepend-icon="mdi-close"
          @click="drawer = false"
        >
          <v-list-item-title>Fermer</v-list-item-title>
        </v-list-item>
        
        <v-divider />
        
        <!-- Mobile Menu Items -->
        <v-list-item to="/" @click="drawer = false">
          <v-list-item-title>Accueil</v-list-item-title>
        </v-list-item>
        
        <v-list-group>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" title="Qui sommes-nous"></v-list-item>
          </template>
          <v-list-item to="/qui-sommes-nous" @click="drawer = false">
            <v-list-item-title>Présentation</v-list-item-title>
          </v-list-item>
          <v-list-item to="/vision-mission-valeurs" @click="drawer = false">
            <v-list-item-title>Vision, Mission, Valeurs</v-list-item-title>
          </v-list-item>
          <v-list-item to="/engagement-politique-rse-dd" @click="drawer = false">
            <v-list-item-title>Engagements - Politique RSE et durabilité</v-list-item-title>
          </v-list-item>
        </v-list-group>

        <v-list-group>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" title="Services"></v-list-item>
          </template>
          <v-list-item to="/strategie-esg-rse" @click="drawer = false">
            <v-list-item-title>Stratégies ESG/RSE</v-list-item-title>
          </v-list-item>
          <v-list-item to="/evaluation-environnementale" @click="drawer = false">
            <v-list-item-title>Évaluations Environnementales</v-list-item-title>
          </v-list-item>
          <v-list-item to="/economie-circulaire" @click="drawer = false">
            <v-list-item-title>Économie circulaire</v-list-item-title>
          </v-list-item>
          <v-list-item to="/neutralite-carbone" @click="drawer = false">
            <v-list-item-title>Neutralité carbone</v-list-item-title>
          </v-list-item>
          <v-list-item to="/biodiversite-ecosystemes" @click="drawer = false">
            <v-list-item-title>Biodiversité et écosystèmes</v-list-item-title>
          </v-list-item>
          <v-list-item to="/reporting-durabilite-esg" @click="drawer = false">
            <v-list-item-title>Reporting durabilité ESG</v-list-item-title>
          </v-list-item>
        </v-list-group>

        <v-list-group>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" title="Notations ESG"></v-list-item>
          </template>
          <v-list-item to="/notation-rating" @click="drawer = false">
            <v-list-item-title>Notation</v-list-item-title>
          </v-list-item>
          <v-list-item to="/labelisation" @click="drawer = false">
            <v-list-item-title>Labellisation</v-list-item-title>
          </v-list-item>
          <v-list-item to="/classement" @click="drawer = false">
            <v-list-item-title>Classement</v-list-item-title>
          </v-list-item>
        </v-list-group>

        <v-list-item to="/formations" @click="drawer = false">
          <v-list-item-title>Formations</v-list-item-title>
        </v-list-item>

        <v-list-group>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" title="Événements"></v-list-item>
          </template>
          <v-list-item to="/africa-corporate-sustainability-conference" @click="drawer = false">
            <v-list-item-title>Conférences</v-list-item-title>
          </v-list-item>
          <v-list-item to="/les-after-work-rse" @click="drawer = false">
            <v-list-item-title>Afterwork RSE</v-list-item-title>
          </v-list-item>
          <v-list-item to="/recompenses" @click="drawer = false">
            <v-list-item-title>Récompenses</v-list-item-title>
          </v-list-item>
        </v-list-group>

        <v-list-group>
          <template v-slot:activator="{ props }">
            <v-list-item v-bind="props" title="Ressources"></v-list-item>
          </template>
          <v-list-item to="/publications" @click="drawer = false">
            <v-list-item-title>Publications</v-list-item-title>
          </v-list-item>
          <v-list-item to="/news-articles" @click="drawer = false">
            <v-list-item-title>News & Articles</v-list-item-title>
          </v-list-item>
          <v-list-item to="/blog" @click="drawer = false">
            <v-list-item-title>Blog</v-list-item-title>
          </v-list-item>
        </v-list-group>

        <v-list-item to="/contact" @click="drawer = false">
          <v-list-item-title>Contact</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Search Overlay -->
    <v-dialog v-model="searchDialog" max-width="600">
      <v-card>
        <v-card-title>
          <span class="text-h5">Rechercher</span>
          <v-spacer />
          <v-btn icon @click="searchDialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="searchQuery"
            label="Que recherchez-vous ?"
            prepend-inner-icon="mdi-magnify"
            variant="outlined"
            @keyup.enter="performSearch"
          />
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn color="primary" @click="performSearch">
            Rechercher
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- Main Content -->
    <v-main>
      <router-view />
    </v-main>

    <!-- Footer -->
    <v-footer color="grey-darken-4" class="text-white">
      <v-container>
        <v-row>
          <!-- Company Info -->
          <v-col cols="12" md="4">
            <v-img
              src="/logo-blanc-transparent.png"
              alt="ESG Stratégies"
              max-height="80"
              max-width="160"
              contain
              class="mb-4"
            />
            <p class="text-body-2">
              Cabinet d'expertise spécialisé en développement durable et compétitivité organisationnelle.
              Nous accompagnons votre transition écologique.
            </p>
          </v-col>

          <!-- Quick Links -->
          <v-col cols="12" md="4">
            <h3 class="text-h6 mb-4">Liens Rapides</h3>
            <v-list color="transparent" class="pa-0">
              <v-list-item
                v-for="item in quickLinks"
                :key="item.title"
                :to="item.to"
                class="pa-1"
              >
                <v-list-item-title class="text-body-2">{{ item.title }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-col>

          <!-- Contact & Newsletter -->
          <v-col cols="12" md="4">
            <h3 class="text-h6 mb-4">Contact</h3>
            <div class="mb-4">
              <p class="text-body-2 mb-1">
                <v-icon size="small" class="mr-2">mdi-map-marker</v-icon>
                Ouagadougou, Burkina Faso
              </p>
              <p class="text-body-2 mb-1">
                <v-icon size="small" class="mr-2">mdi-phone</v-icon>
                +226 05 29 50 28
              </p>
              <p class="text-body-2 mb-1">
                <v-icon size="small" class="mr-2">mdi-phone</v-icon>
                +226 01 69 17 77
              </p>
              <p class="text-body-2">
                <v-icon size="small" class="mr-2">mdi-email</v-icon>
                info@esg-strategies.com
              </p>
            </div>

            <!-- Newsletter -->
            <h4 class="text-subtitle-1 mb-2">Newsletter</h4>
            <v-text-field
              v-model="newsletterEmail"
              label="Votre email"
              variant="outlined"
              density="compact"
              append-inner-icon="mdi-send"
              @click:append-inner="subscribeNewsletter"
              @keyup.enter="subscribeNewsletter"
              class="mb-3"
            />

            <!-- Social Media -->
            <div class="d-flex">
              <v-btn
                v-for="social in socialLinks"
                :key="social.name"
                :icon="social.icon"
                :href="social.url"
                target="_blank"
                variant="text"
                size="small"
                class="mr-2"
              />
            </div>
          </v-col>
        </v-row>

        <v-divider class="my-4" />

        <v-row align="center">
          <v-col cols="12" md="6">
            <p class="text-body-2 mb-0">
              © {{ new Date().getFullYear() }} ESG Stratégies. Tous droits réservés.
            </p>
          </v-col>
          <v-col cols="12" md="6" class="text-md-right">
            <p class="text-body-2 mb-0">
              Développé avec ❤️ pour un avenir durable
            </p>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      drawer: false,
      searchDialog: false,
      searchQuery: '',
      newsletterEmail: '',
      
      quickLinks: [
        { title: 'Nos Services', to: '/nos-services' },
        { title: 'Formations', to: '/formations' },
        { title: 'Publications', to: '/publications' },
        { title: 'Contact', to: '/contact' }
      ],
      
      socialLinks: [
        { name: 'LinkedIn', icon: 'mdi-linkedin', url: '#' },
        { name: 'Twitter', icon: 'mdi-twitter', url: '#' },
        { name: 'Facebook', icon: 'mdi-facebook', url: '#' },
        { name: 'Instagram', icon: 'mdi-instagram', url: '#' }
      ]
    }
  },
  
  methods: {
    performSearch() {
      if (this.searchQuery.trim()) {
        console.log('Recherche:', this.searchQuery)
        // Implémenter la logique de recherche
        this.searchDialog = false
        this.searchQuery = ''
      }
    },
    
    subscribeNewsletter() {
      if (this.newsletterEmail.trim()) {
        console.log('Inscription newsletter:', this.newsletterEmail)
        // Implémenter la logique d'inscription
        this.newsletterEmail = ''
      }
    }
  }
}
</script>

<style scoped>
/* Logo Styles */
.logo-container {
  transition: all 0.3s ease;
  padding: 8px;
  border-radius: 8px;
}

.logo-container:hover {
  background-color: rgba(76, 175, 80, 0.05);
  transform: scale(1.02);
}

.logo-img {
  transition: all 0.3s ease;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.1));
}

.logo-img:hover {
  filter: drop-shadow(0 4px 8px rgba(0, 0, 0, 0.15));
}

/* Mega Menu Styles */
.mega-menu-header {
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1) !important;
  border-bottom: 1px solid #e0e0e0;
}

.mega-menu-container {
  align-items: center;
}

.nav-item {
  font-weight: 500 !important;
  text-transform: none !important;
  letter-spacing: 0.5px;
  transition: all 0.3s ease;
  position: relative;
}

.nav-item:hover {
  background-color: rgba(0, 0, 0, 0.04) !important;
  transform: translateY(-1px);
}

.nav-item::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 0;
  height: 2px;
  background: linear-gradient(45deg, #4CAF50, #2196F3);
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.nav-item:hover::after {
  width: 80%;
}

/* Unified Mega Menu Content Styles */
.mega-menu-content {
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15) !important;
  border-radius: 12px !important;
  border: 1px solid #e0e0e0;
  overflow: hidden;
  margin-top: 8px;
  /* Centrage du mega menu */
  left: 50% !important;
  transform: translateX(-50%) !important;
  position: absolute !important;
}

.mega-menu-card {
  border-radius: 12px !important;
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
  /* Assurer une largeur cohérente */
  min-width: 800px;
}

.mega-menu-item {
  padding: 20px;
  border-radius: 8px;
  transition: all 0.3s ease;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  min-height: 200px;
}

.mega-menu-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
  background: linear-gradient(135deg, #ffffff 0%, #f0f8f0 100%);
}

.mega-menu-item h3 {
  color: #333;
  font-weight: 600;
  text-align: center;
}

.mega-menu-item p {
  color: #666;
  text-align: center;
  line-height: 1.4;
  flex-grow: 1;
}

.mega-menu-item .v-btn {
  margin-top: auto;
  border-radius: 20px;
  font-weight: 500;
  text-transform: none;
  transition: all 0.3s ease;
}

.mega-menu-item .v-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.mega-menu-item .v-icon {
  transition: all 0.3s ease;
}

.mega-menu-item:hover .v-icon {
  transform: scale(1.1);
}

/* Mobile Menu Styles */
.v-navigation-drawer {
  background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
}

.v-navigation-drawer .v-list-group__items .v-list-item {
  padding-left: 32px !important;
  font-size: 0.9rem;
}

.v-navigation-drawer .v-list-item {
  border-radius: 8px;
  margin: 2px 8px;
  transition: all 0.2s ease;
}

.v-navigation-drawer .v-list-item:hover {
  background-color: rgba(76, 175, 80, 0.1) !important;
  transform: translateX(4px);
}

/* Footer Styles */
.v-footer {
  background: linear-gradient(135deg, #263238 0%, #37474f 100%) !important;
}

.v-footer .v-btn {
  transition: all 0.3s ease;
}

.v-footer .v-btn:hover {
  transform: translateY(-2px) scale(1.1);
  background-color: rgba(255, 255, 255, 0.1) !important;
}

/* Search Dialog Styles */
.v-dialog .v-card {
  border-radius: 12px !important;
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15) !important;
}

/* Responsive Design */
@media (max-width: 1264px) {
  .mega-menu-container {
    display: none !important;
  }
}

@media (max-width: 600px) {
  .mega-menu-item {
    padding: 16px;
  }
  
  .mega-menu-item h3 {
    font-size: 1.1rem;
  }
  
  .mega-menu-item p {
    font-size: 0.85rem;
  }
}

/* Animation for menu items */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.dropdown-menu .v-list-item,
.mega-menu-item {
  animation: fadeInUp 0.3s ease forwards;
}

/* Logo hover effect */
.v-img {
  transition: all 0.3s ease;
}

.v-img:hover {
  transform: scale(1.05);
  filter: brightness(1.1);
}

/* Custom scrollbar for mobile menu */
.v-navigation-drawer::-webkit-scrollbar {
  width: 4px;
}

.v-navigation-drawer::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.v-navigation-drawer::-webkit-scrollbar-thumb {
  background: #4CAF50;
  border-radius: 2px;
}

.v-navigation-drawer::-webkit-scrollbar-thumb:hover {
  background: #45a049;
}
</style>