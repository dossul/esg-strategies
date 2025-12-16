<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="8" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Nos Services
            </h1>
            <p class="text-h5 mb-8">
              Accompagnement personnalisé pour votre transformation durable
            </p>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Introduction Section -->
    <section class="py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <div class="text-center mb-12">
              <h2 class="text-h3 font-weight-bold mb-6 text-primary">
                Nos Domaines d'Expertise
              </h2>
            </div>
            
            <v-card elevation="2" class="pa-8 mb-8">
              <p class="text-h6 text-center mb-6">
                ESG Stratégies offre des services de conseil spécialisés aux entreprises, ONG, 
                collectivités territoriales et administrations publiques.
              </p>
              
              <p class="text-body-1 mb-6">
                Notre approche intégrée couvre l'ensemble des enjeux ESG (Environnementaux, Sociaux et de Gouvernance) 
                pour vous accompagner dans votre transition vers des pratiques plus durables et responsables. 
                Nous proposons des solutions sur mesure adaptées à votre secteur d'activité et à vos objectifs spécifiques.
              </p>
              
              <p class="text-body-1">
                Découvrez ci-dessous nos principales catégories de services et n'hésitez pas à nous contacter 
                pour discuter de vos besoins spécifiques.
              </p>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Services Categories Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Nos Catégories de Services
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Des solutions complètes pour tous vos besoins ESG
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="categorie in categoriesServices"
            :key="categorie.title"
            cols="12"
            md="6"
            lg="4"
          >
            <v-card 
              class="service-category-card h-100" 
              elevation="2"
              @click="openCategoryDialog(categorie)"
            >
              <v-card-text class="pa-6 text-center">
                <v-icon
                  :icon="categorie.icon"
                  size="64"
                  :color="categorie.color"
                  class="mb-4"
                />
                <h3 class="text-h5 font-weight-bold mb-4 text-primary">
                  {{ categorie.title }}
                </h3>
                <p class="text-body-1 mb-4">{{ categorie.description }}</p>
                
                <v-btn
                  :color="categorie.color"
                  variant="outlined"
                  class="text-capitalize"
                >
                  En savoir plus
                  <v-icon end>mdi-arrow-right</v-icon>
                </v-btn>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Methodology Section -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Notre Méthodologie
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Une approche structurée pour garantir votre succès
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="(etape, index) in methodologie"
            :key="etape.title"
            cols="12"
            md="6"
            lg="3"
          >
            <div class="methodology-step text-center">
              <div class="step-number mb-4">
                <v-avatar size="80" color="primary">
                  <span class="text-h4 text-white font-weight-bold">
                    {{ index + 1 }}
                  </span>
                </v-avatar>
              </div>
              
              <v-icon
                :icon="etape.icon"
                size="48"
                color="secondary"
                class="mb-4"
              />
              
              <h3 class="text-h6 font-weight-bold mb-3 text-primary">
                {{ etape.title }}
              </h3>
              
              <p class="text-body-2">{{ etape.description }}</p>
            </div>
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
              Prêt à Commencer Votre Transformation ?
            </h2>
            <p class="text-h6 mb-8">
              Contactez-nous pour discuter de vos besoins et découvrir comment nous pouvons 
              vous accompagner dans votre démarche ESG.
            </p>
            <div class="d-flex flex-column flex-md-row justify-center align-center gap-4">
              <v-btn
                to="/contact"
                color="white"
                variant="outlined"
                size="large"
                class="text-capitalize"
              >
                <v-icon left>mdi-email</v-icon>
                Demander un devis
              </v-btn>
              <v-btn
                href="tel:+22625123456"
                color="white"
                variant="flat"
                size="large"
                class="text-capitalize"
              >
                <v-icon left>mdi-phone</v-icon>
                Appelez-nous
              </v-btn>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Category Dialog -->
    <v-dialog v-model="categoryDialog" max-width="800">
      <v-card v-if="selectedCategory">
        <v-card-title class="d-flex align-center">
          <v-icon
            :icon="selectedCategory.icon"
            :color="selectedCategory.color"
            size="32"
            class="mr-3"
          />
          <span class="text-h5">{{ selectedCategory.title }}</span>
          <v-spacer />
          <v-btn
            icon="mdi-close"
            variant="text"
            @click="categoryDialog = false"
          />
        </v-card-title>
        
        <v-card-text class="pa-6">
          <p class="text-body-1 mb-6">{{ selectedCategory.detailedDescription }}</p>
          
          <h4 class="text-h6 font-weight-bold mb-4">Services inclus :</h4>
          <v-list>
            <v-list-item
              v-for="service in selectedCategory.services"
              :key="service"
              class="px-0"
            >
              <template v-slot:prepend>
                <v-icon icon="mdi-check-circle" color="primary" />
              </template>
              <v-list-item-title>{{ service }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-card-text>
        
        <v-card-actions class="pa-6">
          <v-spacer />
          <v-btn
            to="/contact"
            :color="selectedCategory.color"
            variant="flat"
            class="text-capitalize"
          >
            Nous contacter
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'Services',
  data() {
    return {
      categoryDialog: false,
      selectedCategory: null,
      
      categoriesServices: [
        {
          title: 'Environnement et Ressources Naturelles',
          description: 'Gestion durable des ressources et protection de l\'environnement',
          icon: 'mdi-leaf',
          color: 'primary',
          detailedDescription: 'Nous accompagnons les organisations dans la mise en place de stratégies environnementales durables, la gestion optimisée des ressources naturelles et la réduction de leur empreinte écologique.',
          services: [
            'Évaluation d\'impact environnemental',
            'Gestion des déchets et économie circulaire',
            'Stratégies de réduction carbone',
            'Conservation de la biodiversité',
            'Gestion durable de l\'eau',
            'Énergies renouvelables'
          ]
        },
        {
          title: 'Gouvernance',
          description: 'Amélioration des structures de gouvernance et transparence',
          icon: 'mdi-account-group',
          color: 'secondary',
          detailedDescription: 'Nous aidons les organisations à renforcer leurs structures de gouvernance, améliorer la transparence et mettre en place des mécanismes de contrôle efficaces.',
          services: [
            'Audit de gouvernance',
            'Mise en place de comités ESG',
            'Politiques de transparence',
            'Gestion des risques',
            'Conformité réglementaire',
            'Formation des dirigeants'
          ]
        },
        {
          title: 'Société et Impact Social',
          description: 'Développement de l\'impact social et engagement communautaire',
          icon: 'mdi-heart-multiple',
          color: 'accent',
          detailedDescription: 'Nous développons des stratégies pour maximiser l\'impact social positif des organisations et renforcer leur engagement auprès des communautés locales.',
          services: [
            'Programmes de responsabilité sociale',
            'Engagement communautaire',
            'Développement local',
            'Inclusion et diversité',
            'Conditions de travail',
            'Dialogue avec les parties prenantes'
          ]
        },
        {
          title: 'Publications et Recherche',
          description: 'Recherche appliquée et publications spécialisées',
          icon: 'mdi-book-open-variant',
          color: 'neutral',
          detailedDescription: 'Nous produisons des recherches de qualité et des publications spécialisées pour faire avancer les connaissances dans le domaine du développement durable.',
          services: [
            'Études sectorielles',
            'Rapports de recherche',
            'Guides pratiques',
            'Benchmarking',
            'Veille réglementaire',
            'Publications académiques'
          ]
        },
        {
          title: 'Formations',
          description: 'Renforcement des capacités et formation spécialisée',
          icon: 'mdi-school',
          color: 'primary',
          detailedDescription: 'Nous proposons des programmes de formation adaptés pour renforcer les capacités de vos équipes en matière de développement durable et ESG.',
          services: [
            'Formations ESG sur mesure',
            'Ateliers pratiques',
            'Certification professionnelle',
            'Formation de formateurs',
            'E-learning',
            'Accompagnement post-formation'
          ]
        },
        {
          title: 'Conseils en Stratégies RSE et DD',
          description: 'Conseil stratégique en RSE et développement durable',
          icon: 'mdi-strategy',
          color: 'secondary',
          detailedDescription: 'Nous accompagnons les organisations dans l\'élaboration et la mise en œuvre de leurs stratégies RSE et développement durable.',
          services: [
            'Diagnostic RSE',
            'Stratégie de développement durable',
            'Plan d\'action ESG',
            'Indicateurs de performance',
            'Reporting extra-financier',
            'Accompagnement à la certification'
          ]
        }
      ],
      
      methodologie: [
        {
          title: 'Diagnostic',
          description: 'Analyse approfondie de votre situation actuelle et identification des enjeux prioritaires',
          icon: 'mdi-magnify'
        },
        {
          title: 'Stratégie',
          description: 'Élaboration d\'une stratégie personnalisée adaptée à vos objectifs et contraintes',
          icon: 'mdi-lightbulb'
        },
        {
          title: 'Mise en œuvre',
          description: 'Accompagnement dans la mise en place des actions et mesures recommandées',
          icon: 'mdi-cogs'
        },
        {
          title: 'Suivi',
          description: 'Monitoring des résultats et ajustements pour garantir l\'atteinte des objectifs',
          icon: 'mdi-chart-line'
        }
      ]
    }
  },
  
  methods: {
    openCategoryDialog(category) {
      this.selectedCategory = category
      this.categoryDialog = true
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

.service-category-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
}

.service-category-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
}

.methodology-step {
  padding: 2rem 1rem;
}

.step-number {
  position: relative;
}

.gap-4 {
  gap: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
  .display-1 {
    font-size: 2.5rem !important;
  }
  
  .text-h3 {
    font-size: 2rem !important;
  }
  
  .d-flex.flex-md-row {
    flex-direction: column !important;
  }
  
  .d-flex.flex-md-row .v-btn {
    width: 100%;
    margin-bottom: 1rem;
  }
  
  .methodology-step {
    padding: 1rem 0.5rem;
  }
}
</style>