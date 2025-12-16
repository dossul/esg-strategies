<template>
  <div>
    <!-- Hero Slider -->
    <section class="hero-slider">
      <HeroSlider />
    </section>

    <!-- Agence Section -->
    <section class="py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10" class="text-center">
            <h2 class="text-h3 font-weight-bold mb-6 text-primary">
              Agence spécialisée en développement durable et compétitivité organisationnelle
            </h2>
            <h3 class="text-h4 mb-8 text-secondary">
              Accélérer votre transition écologique
            </h3>
            <p class="text-h6 text-grey-darken-1 mb-8">
              ESG Stratégies, cabinet d'expertise, se concentre sur l'analyse des données pour améliorer 
              la gouvernance et promouvoir le développement durable des organisations.
            </p>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Featured Article & Sidebar -->
    <section class="py-16 featured-section bg-grey-lighten-5">
      <v-container>
        <v-row>
          <!-- Featured Article -->
          <v-col cols="12" lg="8">
            <div class="mb-6">
              <h2 class="text-h3 font-weight-bold mb-4 text-primary">Article en vedette</h2>
              <p class="text-h6 text-grey-darken-1">
                Notre sélection de contenu incontournable
              </p>
            </div>
            
            <v-card
              class="featured-article-card"
              elevation="8"
              hover
              :to="featuredArticle.link"
            >
              <v-row no-gutters>
                <v-col cols="12" md="6">
                  <div class="featured-image-container">
                    <v-img
                      :src="featuredArticle.image"
                      :alt="featuredArticle.title"
                      height="400"
                      cover
                      class="featured-image"
                    >
                      <div class="featured-overlay">
                        <v-chip
                          :color="featuredArticle.categoryColor"
                          variant="flat"
                          size="small"
                          class="ma-4"
                        >
                          {{ featuredArticle.category }}
                        </v-chip>
                      </div>
                    </v-img>
                  </div>
                </v-col>
                <v-col cols="12" md="6">
                  <v-card-text class="pa-8 h-100 d-flex flex-column">
                    <div>
                      <h3 class="text-h4 font-weight-bold mb-4 text-primary">
                        {{ featuredArticle.title }}
                      </h3>
                      <div class="d-flex align-center mb-4">
                        <v-icon color="grey" size="small" class="mr-2">mdi-calendar</v-icon>
                        <span class="text-body-2 text-grey-darken-1">{{ featuredArticle.date }}</span>
                      </div>
                      <p class="text-body-1 mb-6">{{ featuredArticle.excerpt }}</p>
                    </div>
                    <div class="mt-auto">
                      <v-btn
                        :to="featuredArticle.link"
                        color="primary"
                        variant="flat"
                        size="large"
                        class="text-capitalize"
                      >
                        Lire l'article complet
                        <v-icon right>mdi-arrow-right</v-icon>
                      </v-btn>
                    </div>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-card>
          </v-col>

          <!-- Sidebar for Ads -->
          <v-col cols="12" lg="4">
            <div class="sidebar-content">
              <!-- Event Ad -->
              <v-card
                class="mb-6 ad-card"
                elevation="4"
                hover
                :href="eventAd.link"
                target="_blank"
              >
                <v-img
                  :src="eventAd.image"
                  :alt="eventAd.title"
                  height="200"
                  cover
                  class="ad-image"
                >
                  <div class="ad-overlay">
                    <v-chip
                      color="red"
                      variant="flat"
                      size="small"
                      class="ma-3"
                    >
                      {{ eventAd.type }}
                    </v-chip>
                  </div>
                </v-img>
                <v-card-text class="pa-4">
                  <h4 class="text-h6 font-weight-bold mb-2 text-primary">
                    {{ eventAd.title }}
                  </h4>
                  <p class="text-body-2 mb-3">{{ eventAd.description }}</p>
                  <div class="d-flex align-center mb-3">
                    <v-icon color="grey" size="small" class="mr-2">mdi-map-marker</v-icon>
                    <span class="text-caption text-grey-darken-1">{{ eventAd.location }}</span>
                  </div>
                  <div class="d-flex align-center">
                    <v-icon color="grey" size="small" class="mr-2">mdi-calendar</v-icon>
                    <span class="text-caption text-grey-darken-1">{{ eventAd.date }}</span>
                  </div>
                </v-card-text>
                <v-card-actions class="pa-4 pt-0">
                  <v-btn
                    :href="eventAd.link"
                    target="_blank"
                    color="red"
                    variant="outlined"
                    size="small"
                    block
                  >
                    Découvrir les awards
                  </v-btn>
                </v-card-actions>
              </v-card>

              <!-- Book Ad -->
              <v-card
                class="ad-card"
                elevation="4"
                hover
                :href="bookAd.link"
                target="_blank"
              >
                <v-img
                  :src="bookAd.image"
                  :alt="bookAd.title"
                  height="200"
                  cover
                  class="ad-image"
                >
                  <div class="ad-overlay">
                    <v-chip
                      color="purple"
                      variant="flat"
                      size="small"
                      class="ma-3"
                    >
                      {{ bookAd.type }}
                    </v-chip>
                  </div>
                </v-img>
                <v-card-text class="pa-4">
                  <h4 class="text-h6 font-weight-bold mb-2 text-primary">
                    {{ bookAd.title }}
                  </h4>
                  <p class="text-body-2 mb-3">{{ bookAd.description }}</p>
                  <div class="d-flex align-center mb-3">
                    <v-icon color="grey" size="small" class="mr-2">mdi-account</v-icon>
                    <span class="text-caption text-grey-darken-1">{{ bookAd.author }}</span>
                  </div>
                  <div class="d-flex align-center">
                    <v-icon color="grey" size="small" class="mr-2">mdi-currency-eur</v-icon>
                    <span class="text-caption text-grey-darken-1">{{ bookAd.price }}</span>
                  </div>
                </v-card-text>
                <v-card-actions class="pa-4 pt-0">
                  <v-btn
                    :href="bookAd.link"
                    target="_blank"
                    color="purple"
                    variant="outlined"
                    size="small"
                    block
                  >
                    Acheter maintenant
                  </v-btn>
                </v-card-actions>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Ads Section -->
    <section class="py-12 bg-white">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-6">
            <h2 class="text-h4 font-weight-bold mb-2 text-primary">Nos Partenaires</h2>
            <p class="text-body-1 text-grey-darken-1">
              Découvrez nos solutions et partenariats stratégiques
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="ad in ads"
            :key="ad.title"
            cols="12"
            sm="6"
            md="4"
            lg="3"
          >
            <v-card
              class="ad-banner-card h-100"
              elevation="3"
              hover
              :href="ad.link"
              target="_blank"
            >
              <v-img
                :src="ad.image"
                :alt="ad.title"
                height="180"
                cover
                class="ad-banner-image"
              >
                <div class="ad-banner-overlay">
                  <v-chip
                    :color="ad.chipColor"
                    variant="flat"
                    size="small"
                    class="ma-2"
                  >
                    {{ ad.type }}
                  </v-chip>
                </div>
              </v-img>
              <v-card-text class="pa-4">
                <h4 class="text-h6 font-weight-bold mb-2 text-primary">
                  {{ ad.title }}
                </h4>
                <p class="text-body-2 mb-3">{{ ad.description }}</p>
                <div class="d-flex align-center" v-if="ad.price">
                  <v-icon color="green" size="small" class="mr-2">mdi-currency-eur</v-icon>
                  <span class="text-caption font-weight-bold text-green">{{ ad.price }}</span>
                </div>
              </v-card-text>
              <v-card-actions class="pa-4 pt-0">
                <v-btn
                  :href="ad.link"
                  target="_blank"
                  :color="ad.buttonColor"
                  variant="outlined"
                  size="small"
                  block
                >
                  {{ ad.buttonText }}
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Articles Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-8">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Articles</h2>
            <p class="text-h6 text-grey-darken-1">
              Découvrez nos derniers articles et insights sur les stratégies ESG
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="article in articles"
            :key="article.title"
            cols="12"
            md="6"
            lg="3"
          >
            <v-card
              class="article-card h-100"
              elevation="2"
              hover
              :to="article.link"
            >
              <!-- Image Zone -->
              <v-img
                :src="article.image"
                :alt="article.title"
                height="200"
                cover
                class="article-image"
              >
                <div class="article-overlay">
                  <v-chip
                    :color="article.categoryColor"
                    size="small"
                    class="ma-2"
                  >
                    {{ article.category }}
                  </v-chip>
                </div>
              </v-img>
              
              <v-card-title class="text-h6 font-weight-bold text-primary">
                {{ article.title }}
              </v-card-title>
              <v-card-subtitle class="text-body-2 text-grey-darken-1">
                {{ article.date }}
              </v-card-subtitle>
              <v-card-text>
                <p class="text-body-2">{{ article.excerpt }}</p>
              </v-card-text>
              <v-card-actions>
                <v-btn
                  :to="article.link"
                  color="primary"
                  variant="text"
                  size="small"
                >
                  Lire la suite
                  <v-icon right>mdi-arrow-right</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Services Overview -->
    <section class="py-16 services-section">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-8">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Nos Services</h2>
            <p class="text-h6 text-grey-darken-1">
              Des solutions complètes pour votre transition ESG
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="service in services"
            :key="service.title"
            cols="12"
            md="6"
            lg="4"
          >
            <v-card
              class="service-card h-100 text-center"
              elevation="2"
              hover
              :to="service.link"
            >
              <v-card-text class="pa-8">
                <v-icon
                  :icon="service.icon"
                  size="64"
                  :color="service.color"
                  class="mb-4"
                />
                <h3 class="text-h5 font-weight-bold mb-4 text-primary">
                  {{ service.title }}
                </h3>
                <p class="text-body-1">{{ service.description }}</p>
              </v-card-text>
              <v-card-actions class="justify-center pb-6">
                <v-btn
                  :to="service.link"
                  :color="service.color"
                  variant="outlined"
                >
                  En savoir plus
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- CTA Section -->
    <section class="py-16 bg-primary">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8" class="text-center text-white">
            <h2 class="text-h3 font-weight-bold mb-6">
              Prêt à transformer votre organisation ?
            </h2>
            <p class="text-h6 mb-8">
              Contactez-nous pour discuter de vos besoins en stratégies ESG et développement durable
            </p>
            <v-btn
              to="/contact"
              color="white"
              variant="outlined"
              size="large"
              class="text-capitalize mr-4"
            >
              Nous contacter
            </v-btn>
            <v-btn
              href="https://esg-strategies.com/blog/"
              target="_blank"
              color="white"
              variant="flat"
              size="large"
              class="text-capitalize"
            >
              Visiter notre blog
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </section>
  </div>
</template>

<script>
import HeroSlider from '@/components/HeroSlider.vue'

export default {
  name: 'Home',
  components: {
    HeroSlider
  },
  data() {
    return {
      // Articles basés sur le contenu d'Accueil.md
      articles: [
        {
          title: 'Conseils en stratégies RSE et DD',
          category: 'Conseils',
          categoryColor: 'green',
          date: 'janvier 12, 2022',
          excerpt: 'Découvrez nos conseils pour développer des stratégies RSE et de développement durable efficaces.',
          image: '/assets/durabilite-environnement-eco-friendly-concept.jpg',
          link: '/conseil-strategie-rse-dd'
        },
        {
          title: 'Formations',
          category: 'Formations',
          categoryColor: 'blue',
          date: 'octobre 6, 2020',
          excerpt: 'Formez vos équipes aux enjeux ESG et aux meilleures pratiques du développement durable.',
          image: '/assets/groupe-photos-personnes-travaillant-plan-affaires-dans-bureau_812426-65565.jpg',
          link: '/formations'
        },
        {
          title: 'Publications',
          category: 'Publications',
          categoryColor: 'purple',
          date: 'février 5, 2020',
          excerpt: 'Consultez nos publications et études sur les tendances ESG et le développement durable.',
          image: '/assets/Black-And-White-Minimalist-Modern-Pricing-Table-Comparison-Graph-1.png',
          link: '/publications'
        },
        {
          title: 'Société',
          category: 'Société',
          categoryColor: 'orange',
          date: 'janvier 14, 2020',
          excerpt: 'Explorez les enjeux sociétaux et leur impact sur les organisations modernes.',
          image: '/assets/portrait-femme-affaires-elegante-professionnelle_23-2150917266.jpg',
          link: '/societe'
        }
      ],
      
      // Article en vedette
      featuredArticle: {
        title: 'Conseils en stratégies RSE et DD',
        category: 'Conseils',
        categoryColor: 'green',
        date: '12 janvier 2024',
        excerpt: 'ESG STRATEGIE vous aide à intégrer de manière efficace et durable les principes de la Responsabilité Sociale des Entreprises (RSE) et du Développement Durable (DD) dans vos opérations et votre culture d\'entreprise. Découvrez nos services d\'évaluation, de développement de stratégies sur mesure et de mise en œuvre.',
        image: '/assets/durabilite-environnement-eco-friendly-concept.jpg',
        link: '/conseil-strategie-rse-dd'
      },

      // Publicité pour événement - Awards
      eventAd: {
        type: 'AWARDS',
        title: 'African Business & Social Responsibility Awards',
        description: 'Récompenser chaque année des entreprises menant des projets exemplaires et innovants dans le domaine du Développement Durable.',
        location: 'Cérémonie de remise des prix',
        date: 'Candidatures ouvertes',
        image: '/assets/img001-1-11.jpg',
        link: '/recompenses'
      },

      // Publicité pour livre
      bookAd: {
        type: 'PUBLICATION',
        title: 'Guide ESG pour Dirigeants',
        description: 'Le manuel complet pour intégrer les critères ESG dans votre stratégie d\'entreprise.',
        author: 'Dr. Marie Dubois',
        price: '29,99 €',
        image: '/assets/esg-guide-book-cover.svg',
        link: 'https://esg-strategies.com/boutique/guide-esg-dirigeants'
      },
      
      // Ads data
      ads: [
        {
          type: 'FORMATION',
          title: 'Certification ESG Manager',
          description: 'Devenez expert en stratégies ESG avec notre formation certifiante.',
          image: '/assets/formation-esg-certification.svg',
          link: 'https://esg-strategies.com/formations/certification-esg-manager',
          price: '1,299 €',
          chipColor: 'blue',
          buttonColor: 'blue',
          buttonText: 'S\'inscrire'
        },
        {
          type: 'CONSULTATION',
          title: 'Audit ESG Gratuit',
          description: 'Évaluation complète de votre maturité ESG par nos experts.',
          image: '/assets/audit-esg-gratuit.svg',
          link: 'https://esg-strategies.com/audit-gratuit',
          chipColor: 'green',
          buttonColor: 'green',
          buttonText: 'Demander un audit'
        },
        {
          type: 'OUTIL',
          title: 'Plateforme ESG Analytics',
          description: 'Tableau de bord intelligent pour piloter vos indicateurs ESG.',
          image: '/assets/plateforme-esg-analytics.svg',
          link: 'https://esg-strategies.com/plateforme-analytics',
          price: 'À partir de 99 €/mois',
          chipColor: 'purple',
          buttonColor: 'purple',
          buttonText: 'Essai gratuit'
        },
        {
          type: 'ÉVÉNEMENT',
          title: 'Sommet ESG 2024',
          description: 'Le plus grand événement francophone sur les stratégies ESG.',
          image: '/assets/sommet-esg-2024.svg',
          link: 'https://esg-strategies.com/sommet-2024',
          price: '299 €',
          chipColor: 'orange',
          buttonColor: 'orange',
          buttonText: 'Réserver'
        }
      ],
      
      // Services principaux
      services: [
        {
          title: 'Environnement et Ressources',
          description: 'Gestion durable des ressources naturelles et impact environnemental',
          icon: 'mdi-leaf',
          color: 'green',
          link: '/environnement-et-ressources-naturelles'
        },
        {
          title: 'Gouvernance',
          description: 'Amélioration des pratiques de gouvernance et transparence',
          icon: 'mdi-account-group',
          color: 'red',
          link: '/gouvernance'
        },
        {
          title: 'Société',
          description: 'Impact social et engagement communautaire',
          icon: 'mdi-heart-multiple',
          color: 'orange',
          link: '/societe'
        },
        {
          title: 'Formations',
          description: 'Programmes de formation sur les enjeux ESG',
          icon: 'mdi-school',
          color: 'blue',
          link: '/formations'
        },
        {
          title: 'Conseil RSE/DD',
          description: 'Accompagnement stratégique en RSE et développement durable',
          icon: 'mdi-lightbulb',
          color: 'purple',
          link: '/conseil-strategie-rse-dd'
        },
        {
          title: 'Publications',
          description: 'Études et rapports sur les tendances ESG',
          icon: 'mdi-book-open',
          color: 'teal',
          link: '/publications'
        }
      ]
    }
  },
  methods: {
    scrollToServices() {
      const servicesSection = document.querySelector('.services-section')
      if (servicesSection) {
        servicesSection.scrollIntoView({ 
          behavior: 'smooth',
          block: 'start'
        })
      }
    }
  }
}
</script>

<style scoped>
/* Hero Section */
.hero-slider {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

/* Cards Hover Effects */
.article-card,
.service-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.article-card:hover,
.service-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.15);
}

/* Article Image Styles */
.article-image {
  position: relative;
  transition: transform 0.3s ease;
}

.article-card:hover .article-image {
  transform: scale(1.05);
}

.article-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0,0,0,0.3) 0%,
    rgba(0,0,0,0) 50%,
    rgba(0,0,0,0.2) 100%
  );
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}

/* Responsive adjustments */
@media (max-width: 960px) {
  .article-card:hover {
    transform: none;
  }
  
  .article-card:hover .article-image {
    transform: none;
  }
}

/* Featured Article Section */
.featured-section {
  background: linear-gradient(135deg, #f5f5f5 0%, #e8f5e8 100%);
}

.featured-article-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-radius: 16px;
  overflow: hidden;
}

.featured-article-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 60px rgba(0,0,0,0.15);
}

.featured-image-container {
  position: relative;
  overflow: hidden;
}

.featured-image {
  transition: transform 0.3s ease;
}

.featured-article-card:hover .featured-image {
  transform: scale(1.03);
}

.featured-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0,0,0,0.4) 0%,
    rgba(0,0,0,0) 50%,
    rgba(0,0,0,0.3) 100%
  );
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}

/* Sidebar Ads */
.sidebar-content {
  position: sticky;
  top: 100px;
}

.ad-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-radius: 12px;
  overflow: hidden;
}

.ad-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.12);
}

.ad-image {
  transition: transform 0.3s ease;
}

.ad-card:hover .ad-image {
  transform: scale(1.02);
}

/* Ads Banner Section */
.ad-banner-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #e0e0e0;
}

.ad-banner-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.15);
  border-color: transparent;
}

.ad-banner-image {
  transition: transform 0.3s ease;
}

.ad-banner-card:hover .ad-banner-image {
  transform: scale(1.05);
}

.ad-banner-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0,0,0,0.3) 0%,
    rgba(0,0,0,0) 50%,
    rgba(0,0,0,0.2) 100%
  );
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}

/* Responsive adjustments for ads */
@media (max-width: 600px) {
  .ad-banner-card:hover {
    transform: translateY(-2px);
  }
  
  .ad-banner-card:hover .ad-banner-image {
    transform: scale(1.02);
  }
}

.ad-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    to bottom,
    rgba(0,0,0,0.3) 0%,
    rgba(0,0,0,0) 70%,
    rgba(0,0,0,0.2) 100%
  );
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}

/* Mobile responsiveness for featured section */
@media (max-width: 1280px) {
  .sidebar-content {
    position: static;
    top: auto;
  }
}

@media (max-width: 960px) {
  .featured-article-card:hover {
    transform: none;
  }
  
  .featured-article-card:hover .featured-image {
    transform: none;
  }
  
  .ad-card:hover {
    transform: none;
  }
  
  .ad-card:hover .ad-image {
    transform: none;
  }
}
</style>