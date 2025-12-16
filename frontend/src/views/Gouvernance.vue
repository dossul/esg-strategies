<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="8" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Gouvernance d'Entreprise
            </h1>
            <p class="text-h5 mb-8">
              Renforcer la transparence, l'éthique et la performance de votre organisation
            </p>
            <v-btn
              to="/contact"
              color="white"
              variant="outlined"
              size="large"
              class="text-capitalize"
            >
              <v-icon left>mdi-handshake</v-icon>
              Nous consulter
            </v-btn>
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
                Excellence en Gouvernance
              </h2>
              <p class="text-h6 text-grey-darken-1">
                La gouvernance d'entreprise constitue le pilier fondamental d'une organisation durable et performante. 
                Nos experts vous accompagnent dans la mise en place de structures de gouvernance robustes et transparentes.
              </p>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Services de Gouvernance -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Nos Services de Gouvernance
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Des solutions complètes pour optimiser votre gouvernance
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="service in servicesGouvernance"
            :key="service.id"
            cols="12"
            md="6"
            lg="4"
            class="mb-6"
          >
            <v-card class="service-card h-100" elevation="2" hover>
              <v-card-text class="pa-6 text-center">
                <v-icon
                  :icon="service.icon"
                  :color="service.color"
                  size="64"
                  class="mb-4"
                />
                <h3 class="text-h5 font-weight-bold mb-4 text-primary">
                  {{ service.title }}
                </h3>
                <p class="text-body-1 mb-4">{{ service.description }}</p>
                
                <v-list class="bg-transparent">
                  <v-list-item
                    v-for="element in service.elements"
                    :key="element"
                    class="pa-0 mb-1"
                    density="compact"
                  >
                    <template v-slot:prepend>
                      <v-icon 
                        icon="mdi-check-circle" 
                        :color="service.color" 
                        size="16" 
                        class="mr-2"
                      />
                    </template>
                    <v-list-item-title class="text-body-2 text-left">
                      {{ element }}
                    </v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Principes de Gouvernance -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Principes Fondamentaux
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Les piliers d'une gouvernance efficace
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="principe in principesGouvernance"
            :key="principe.id"
            cols="12"
            md="6"
            lg="3"
          >
            <div class="text-center mb-6">
              <v-avatar
                :color="principe.color"
                size="80"
                class="mb-4"
              >
                <v-icon
                  :icon="principe.icon"
                  size="40"
                  color="white"
                />
              </v-avatar>
              <h3 class="text-h6 font-weight-bold mb-3 text-primary">
                {{ principe.title }}
              </h3>
              <p class="text-body-2">{{ principe.description }}</p>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Processus de Mise en Œuvre -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Notre Approche
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Une méthodologie éprouvée en 4 étapes
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="(etape, index) in processus"
            :key="etape.id"
            cols="12"
            md="6"
            lg="3"
          >
            <div class="text-center position-relative">
              <div class="step-number mb-4">
                <v-avatar
                  color="primary"
                  size="60"
                >
                  <span class="text-h4 font-weight-bold text-white">
                    {{ index + 1 }}
                  </span>
                </v-avatar>
              </div>
              
              <v-icon
                :icon="etape.icon"
                color="secondary"
                size="48"
                class="mb-3"
              />
              
              <h3 class="text-h6 font-weight-bold mb-3 text-primary">
                {{ etape.title }}
              </h3>
              <p class="text-body-2">{{ etape.description }}</p>
              
              <!-- Connector line (except for last item) -->
              <div 
                v-if="index < processus.length - 1"
                class="connector-line d-none d-lg-block"
              />
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Avantages -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" md="6">
            <h2 class="text-h3 font-weight-bold mb-6 text-primary">
              Pourquoi Investir dans la Gouvernance ?
            </h2>
            
            <v-list class="bg-transparent">
              <v-list-item
                v-for="avantage in avantages"
                :key="avantage.title"
                class="pa-0 mb-4"
              >
                <template v-slot:prepend>
                  <v-icon 
                    :icon="avantage.icon"
                    color="primary" 
                    size="24" 
                    class="mr-4"
                  />
                </template>
                <div>
                  <v-list-item-title class="text-h6 font-weight-bold text-primary mb-1">
                    {{ avantage.title }}
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-body-1">
                    {{ avantage.description }}
                  </v-list-item-subtitle>
                </div>
              </v-list-item>
            </v-list>
          </v-col>
          
          <v-col cols="12" md="6">
            <v-card elevation="2" class="pa-6">
              <h3 class="text-h5 font-weight-bold mb-4 text-center text-primary">
                Statistiques Clés
              </h3>
              
              <div
                v-for="stat in statistiques"
                :key="stat.label"
                class="d-flex align-center justify-space-between mb-4"
              >
                <div>
                  <div class="text-h4 font-weight-bold text-primary">
                    {{ stat.value }}
                  </div>
                  <div class="text-body-2 text-grey-darken-1">
                    {{ stat.label }}
                  </div>
                </div>
                <v-icon
                  :icon="stat.icon"
                  color="primary"
                  size="32"
                />
              </div>
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
              Renforcez Votre Gouvernance
            </h2>
            <p class="text-h6 mb-8">
              Nos experts sont prêts à vous accompagner dans l'amélioration de votre gouvernance d'entreprise.
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
                Demander une consultation
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
  </div>
</template>

<script>
export default {
  name: 'Gouvernance',
  data() {
    return {
      servicesGouvernance: [
        {
          id: 1,
          title: 'Audit de Gouvernance',
          description: 'Évaluation complète de vos structures et processus de gouvernance',
          icon: 'mdi-clipboard-check',
          color: 'primary',
          elements: [
            'Analyse des organes de gouvernance',
            'Évaluation des processus décisionnels',
            'Revue des politiques et procédures',
            'Identification des axes d\'amélioration'
          ]
        },
        {
          id: 2,
          title: 'Conseil Stratégique',
          description: 'Accompagnement dans la définition et mise en œuvre de votre stratégie',
          icon: 'mdi-strategy',
          color: 'secondary',
          elements: [
            'Élaboration de la stratégie d\'entreprise',
            'Définition des objectifs et KPI',
            'Planification stratégique',
            'Suivi et évaluation des performances'
          ]
        },
        {
          id: 3,
          title: 'Gestion des Risques',
          description: 'Mise en place de systèmes robustes de gestion des risques',
          icon: 'mdi-shield-check',
          color: 'accent',
          elements: [
            'Cartographie des risques',
            'Évaluation et priorisation',
            'Plans de mitigation',
            'Systèmes de surveillance'
          ]
        },
        {
          id: 4,
          title: 'Conformité Réglementaire',
          description: 'Assurance du respect des exigences légales et réglementaires',
          icon: 'mdi-gavel',
          color: 'primary',
          elements: [
            'Veille réglementaire',
            'Mise en conformité',
            'Procédures de contrôle',
            'Formation des équipes'
          ]
        },
        {
          id: 5,
          title: 'Éthique et Intégrité',
          description: 'Développement d\'une culture d\'éthique et d\'intégrité',
          icon: 'mdi-heart-handshake',
          color: 'secondary',
          elements: [
            'Code d\'éthique et de conduite',
            'Programmes de sensibilisation',
            'Mécanismes de signalement',
            'Investigation et sanctions'
          ]
        },
        {
          id: 6,
          title: 'Transparence et Communication',
          description: 'Amélioration de la transparence et de la communication',
          icon: 'mdi-bullhorn',
          color: 'accent',
          elements: [
            'Rapports de gouvernance',
            'Communication aux parties prenantes',
            'Politique de divulgation',
            'Relations investisseurs'
          ]
        }
      ],
      
      principesGouvernance: [
        {
          id: 1,
          title: 'Transparence',
          description: 'Divulgation claire et complète des informations importantes',
          icon: 'mdi-eye',
          color: 'primary'
        },
        {
          id: 2,
          title: 'Responsabilité',
          description: 'Obligation de rendre compte des décisions et actions',
          icon: 'mdi-account-check',
          color: 'secondary'
        },
        {
          id: 3,
          title: 'Équité',
          description: 'Traitement juste et équitable de toutes les parties prenantes',
          icon: 'mdi-scale-balance',
          color: 'accent'
        },
        {
          id: 4,
          title: 'Intégrité',
          description: 'Conduite éthique et respect des valeurs organisationnelles',
          icon: 'mdi-shield-star',
          color: 'primary'
        }
      ],
      
      processus: [
        {
          id: 1,
          title: 'Diagnostic',
          description: 'Évaluation de l\'état actuel de votre gouvernance',
          icon: 'mdi-magnify'
        },
        {
          id: 2,
          title: 'Conception',
          description: 'Élaboration d\'un plan d\'amélioration personnalisé',
          icon: 'mdi-drawing'
        },
        {
          id: 3,
          title: 'Mise en Œuvre',
          description: 'Déploiement des nouvelles structures et processus',
          icon: 'mdi-cogs'
        },
        {
          id: 4,
          title: 'Suivi',
          description: 'Monitoring continu et ajustements nécessaires',
          icon: 'mdi-chart-line'
        }
      ],
      
      avantages: [
        {
          title: 'Amélioration de la Performance',
          description: 'Une meilleure gouvernance conduit à une performance organisationnelle supérieure',
          icon: 'mdi-trending-up'
        },
        {
          title: 'Réduction des Risques',
          description: 'Identification et mitigation proactive des risques opérationnels et stratégiques',
          icon: 'mdi-shield-check'
        },
        {
          title: 'Confiance des Investisseurs',
          description: 'Renforcement de la confiance et attraction de nouveaux investissements',
          icon: 'mdi-handshake'
        },
        {
          title: 'Conformité Réglementaire',
          description: 'Respect des exigences légales et évitement des sanctions',
          icon: 'mdi-gavel'
        },
        {
          title: 'Réputation Renforcée',
          description: 'Amélioration de l\'image de marque et de la réputation',
          icon: 'mdi-star'
        }
      ],
      
      statistiques: [
        {
          value: '85%',
          label: 'des entreprises voient leur performance s\'améliorer',
          icon: 'mdi-chart-line'
        },
        {
          value: '70%',
          label: 'de réduction des risques opérationnels',
          icon: 'mdi-shield-check'
        },
        {
          value: '90%',
          label: 'de satisfaction client avec nos services',
          icon: 'mdi-star'
        },
        {
          value: '15+',
          label: 'années d\'expérience en gouvernance',
          icon: 'mdi-calendar-check'
        }
      ]
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

.service-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.service-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
}

.step-number {
  position: relative;
}

.connector-line {
  position: absolute;
  top: 30px;
  right: -50%;
  width: 100%;
  height: 2px;
  background: linear-gradient(to right, #1976d2, transparent);
  z-index: 0;
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
  
  .connector-line {
    display: none !important;
  }
}
</style>