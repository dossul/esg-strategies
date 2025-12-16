<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="8" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Blog ESG Stratégies
            </h1>
            <p class="text-h5 mb-8">
              Actualités, analyses et insights sur les enjeux ESG
            </p>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Articles Section -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Nos Derniers Articles
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Découvrez nos analyses et conseils d'experts
            </p>
          </v-col>
        </v-row>

        <!-- Filter Tabs -->
        <v-row class="mb-8">
          <v-col cols="12">
            <v-tabs
              v-model="activeTab"
              color="primary"
              align-tabs="center"
              class="mb-6"
            >
              <v-tab value="all">Tous les articles</v-tab>
              <v-tab value="environnement">Environnement</v-tab>
              <v-tab value="social">Social</v-tab>
              <v-tab value="gouvernance">Gouvernance</v-tab>
              <v-tab value="formations">Formations</v-tab>
            </v-tabs>
          </v-col>
        </v-row>

        <!-- Articles Grid -->
        <v-row>
          <v-col
            v-for="article in filteredArticles"
            :key="article.id"
            cols="12"
            md="6"
            lg="4"
          >
            <v-card class="article-card h-100" elevation="2" hover>
              <v-img
                :src="article.image"
                height="200"
                cover
                class="article-image"
              >
                <div class="article-overlay">
                  <v-chip
                    :color="getCategoryColor(article.category)"
                    size="small"
                    class="ma-2"
                  >
                    {{ article.category }}
                  </v-chip>
                </div>
              </v-img>
              
              <v-card-text class="pa-6">
                <div class="d-flex align-center mb-3">
                  <v-icon icon="mdi-calendar" size="16" class="mr-2 text-grey" />
                  <span class="text-caption text-grey">{{ formatDate(article.date) }}</span>
                  <v-spacer />
                  <v-icon icon="mdi-clock-outline" size="16" class="mr-1 text-grey" />
                  <span class="text-caption text-grey">{{ article.readTime }} min</span>
                </div>
                
                <h3 class="text-h6 font-weight-bold mb-3 text-primary">
                  {{ article.title }}
                </h3>
                
                <p class="text-body-2 text-grey-darken-1 mb-4">
                  {{ article.excerpt }}
                </p>
                
                <div class="d-flex align-center">
                  <v-avatar size="32" class="mr-3">
                    <v-img :src="article.author.avatar" />
                  </v-avatar>
                  <div>
                    <div class="text-body-2 font-weight-medium">{{ article.author.name }}</div>
                    <div class="text-caption text-grey">{{ article.author.role }}</div>
                  </div>
                </div>
              </v-card-text>
              
              <v-card-actions class="pa-6 pt-0">
                <v-btn
                  :to="`/blog/${article.slug}`"
                  color="primary"
                  variant="outlined"
                  class="text-capitalize"
                  block
                >
                  Lire l'article
                  <v-icon end>mdi-arrow-right</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>

        <!-- Load More Button -->
        <v-row v-if="hasMoreArticles" class="mt-8">
          <v-col cols="12" class="text-center">
            <v-btn
              color="primary"
              variant="outlined"
              size="large"
              @click="loadMoreArticles"
              :loading="loadingMore"
            >
              Charger plus d'articles
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Newsletter Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8" class="text-center">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Restez Informé
            </h2>
            <p class="text-h6 mb-8 text-grey-darken-1">
              Abonnez-vous à notre newsletter pour recevoir nos derniers articles et analyses
            </p>
            
            <v-card elevation="2" class="pa-8">
              <v-form @submit.prevent="subscribeNewsletter">
                <v-row align="center">
                  <v-col cols="12" md="8">
                    <v-text-field
                      v-model="email"
                      label="Votre adresse email"
                      type="email"
                      variant="outlined"
                      required
                      :rules="emailRules"
                    />
                  </v-col>
                  <v-col cols="12" md="4">
                    <v-btn
                      type="submit"
                      color="primary"
                      size="large"
                      block
                      :loading="subscribing"
                    >
                      S'abonner
                    </v-btn>
                  </v-col>
                </v-row>
              </v-form>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Blog',
  data() {
    return {
      activeTab: 'all',
      email: '',
      subscribing: false,
      loadingMore: false,
      hasMoreArticles: true,
      
      emailRules: [
        v => !!v || 'L\'email est requis',
        v => /.+@.+\..+/.test(v) || 'L\'email doit être valide'
      ],
      
      articles: [
        {
          id: 1,
          title: 'Les enjeux de la transition écologique en Afrique de l\'Ouest',
          excerpt: 'Analyse des défis et opportunités pour les entreprises dans leur démarche de transition écologique en Afrique de l\'Ouest.',
          category: 'Environnement',
          date: '2024-01-15',
          readTime: 8,
          image: '/src/assets/images/environment-hero.svg',
          slug: 'transition-ecologique-afrique-ouest',
          author: {
            name: 'Dr. Amadou Diallo',
            role: 'Expert Environnement',
            avatar: '/src/assets/images/Logo_ESG_blanc-transparent.png'
          }
        },
        {
          id: 2,
          title: 'Gouvernance d\'entreprise et transparence : les nouvelles exigences',
          excerpt: 'Comment les entreprises peuvent-elles améliorer leur gouvernance pour répondre aux attentes croissantes de transparence.',
          category: 'Gouvernance',
          date: '2024-01-10',
          readTime: 6,
          image: '/src/assets/images/governance-hero.svg',
          slug: 'gouvernance-transparence-exigences',
          author: {
            name: 'Marie Ouédraogo',
            role: 'Consultante Gouvernance',
            avatar: '/src/assets/images/Logo_ESG_blanc-transparent.png'
          }
        },
        {
          id: 3,
          title: 'Impact social des entreprises : mesurer pour mieux agir',
          excerpt: 'Méthodologies et outils pour évaluer et améliorer l\'impact social des activités entrepreneuriales.',
          category: 'Social',
          date: '2024-01-05',
          readTime: 7,
          image: '/src/assets/images/social-hero.svg',
          slug: 'impact-social-mesurer-agir',
          author: {
            name: 'Ibrahim Sawadogo',
            role: 'Spécialiste Impact Social',
            avatar: '/src/assets/images/Logo_ESG_blanc-transparent.png'
          }
        },
        {
          id: 4,
          title: 'Formation ESG : développer les compétences de demain',
          excerpt: 'L\'importance de la formation continue en matière ESG pour préparer les équipes aux défis futurs.',
          category: 'Formations',
          date: '2023-12-28',
          readTime: 5,
          image: '/src/assets/images/strategy-hero.svg',
          slug: 'formation-esg-competences-demain',
          author: {
            name: 'Fatou Traoré',
            role: 'Responsable Formation',
            avatar: '/src/assets/images/Logo_ESG_blanc-transparent.png'
          }
        },
        {
          id: 5,
          title: 'Économie circulaire : opportunités pour les PME africaines',
          excerpt: 'Comment les petites et moyennes entreprises peuvent tirer parti des principes de l\'économie circulaire.',
          category: 'Environnement',
          date: '2023-12-20',
          readTime: 9,
          image: '/src/assets/images/environment-hero.svg',
          slug: 'economie-circulaire-pme-africaines',
          author: {
            name: 'Dr. Amadou Diallo',
            role: 'Expert Environnement',
            avatar: '/src/assets/images/Logo_ESG_blanc-transparent.png'
          }
        },
        {
          id: 6,
          title: 'Dialogue social et engagement des parties prenantes',
          excerpt: 'Stratégies pour améliorer le dialogue avec les communautés locales et les parties prenantes.',
          category: 'Social',
          date: '2023-12-15',
          readTime: 6,
          image: '/src/assets/images/social-hero.svg',
          slug: 'dialogue-social-parties-prenantes',
          author: {
            name: 'Ibrahim Sawadogo',
            role: 'Spécialiste Impact Social',
            avatar: '/src/assets/images/Logo_ESG_blanc-transparent.png'
          }
        }
      ]
    }
  },
  
  computed: {
    filteredArticles() {
      if (this.activeTab === 'all') {
        return this.articles
      }
      return this.articles.filter(article => 
        article.category.toLowerCase() === this.activeTab.toLowerCase()
      )
    }
  },
  
  methods: {
    getCategoryColor(category) {
      const colors = {
        'Environnement': 'primary',
        'Social': 'accent',
        'Gouvernance': 'secondary',
        'Formations': 'neutral'
      }
      return colors[category] || 'grey'
    },
    
    formatDate(dateString) {
      const options = { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
      }
      return new Date(dateString).toLocaleDateString('fr-FR', options)
    },
    
    async subscribeNewsletter() {
      this.subscribing = true
      try {
        // Simulation d'un appel API
        await new Promise(resolve => setTimeout(resolve, 1000))
        this.$toast.success('Inscription réussie ! Merci de votre intérêt.')
        this.email = ''
      } catch (error) {
        this.$toast.error('Erreur lors de l\'inscription. Veuillez réessayer.')
      } finally {
        this.subscribing = false
      }
    },
    
    async loadMoreArticles() {
      this.loadingMore = true
      try {
        // Simulation d'un appel API pour charger plus d'articles
        await new Promise(resolve => setTimeout(resolve, 1000))
        // Ici, vous ajouteriez les nouveaux articles à this.articles
        this.hasMoreArticles = false // Pour cet exemple
      } catch (error) {
        this.$toast.error('Erreur lors du chargement des articles.')
      } finally {
        this.loadingMore = false
      }
    }
  }
}
</script>

<style scoped>
.hero-section {
  min-height: 400px;
  display: flex;
  align-items: center;
}

.article-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.article-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
}

.article-image {
  position: relative;
}

.article-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(to bottom, rgba(0,0,0,0.3) 0%, transparent 50%);
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
}

/* Responsive */
@media (max-width: 768px) {
  .display-1 {
    font-size: 2.5rem !important;
  }
  
  .text-h3 {
    font-size: 2rem !important;
  }
}
</style>