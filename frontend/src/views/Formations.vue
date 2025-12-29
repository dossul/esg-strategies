<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="8" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Formations ESG
            </h1>
            <p class="text-h5 mb-8">
              Accélérer la montée en compétences de vos collaborateurs grâce à nos formations spécialisées
            </p>
            <v-btn
              color="white"
              variant="outlined"
              size="large"
              class="text-capitalize"
              @click="downloadCatalog"
            >
              <v-icon left>mdi-download</v-icon>
              Télécharger notre catalogue 2024
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Catégories de Formations Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Nos Catégories de Formations
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Des programmes structurés pour tous les niveaux
            </p>
          </v-col>
        </v-row>
        
        <v-row class="mb-8">
          <v-col
            v-for="categorie in categoriesFormation"
            :key="categorie.title"
            cols="12"
            md="4"
          >
            <v-card class="category-card h-100 text-center" elevation="3" hover>
              <v-card-text class="pa-8">
                <v-icon
                  :icon="categorie.icon"
                  size="72"
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
                  @click="scrollToCategory(categorie.id)"
                >
                  Découvrir
                  <v-icon end>mdi-arrow-down</v-icon>
                </v-btn>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Public Cible Section -->
    <section class="py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <div class="text-center mb-12">
              <h2 class="text-h3 font-weight-bold mb-6 text-primary">
                Public Cible
              </h2>
            </div>
            
            <v-card elevation="2" class="pa-8 mb-8">
              <p class="text-h6 text-center mb-6">
                Nos formations s'adressent principalement aux cadres des secteurs privés et publics ainsi que la société civile.
              </p>
              
              <v-row>
                <v-col
                  v-for="target in publicCible"
                  :key="target.title"
                  cols="12"
                  md="6"
                  lg="3"
                >
                  <div class="text-center">
                    <v-icon
                      :icon="target.icon"
                      size="48"
                      color="primary"
                      class="mb-3"
                    />
                    <h4 class="text-h6 font-weight-bold text-primary">
                      {{ target.title }}
                    </h4>
                  </div>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Certifications Internationales Section -->
    <section id="certifications-internationales" class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <v-icon icon="mdi-certificate" size="64" color="primary" class="mb-4" />
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Certifications Internationales
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Formations certifiantes conformes aux standards internationaux
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="formation in formations"
            :key="formation.id"
            cols="12"
            lg="6"
            class="mb-6"
          >
            <v-card class="formation-card h-100" elevation="2" hover>
              <v-card-text class="pa-6">
                <div class="d-flex align-center mb-4">
                  <v-icon
                    :icon="formation.icon"
                    :color="formation.color"
                    size="40"
                    class="mr-4"
                  />
                  <div>
                    <h3 class="text-h5 font-weight-bold text-primary mb-1">
                      {{ formation.title }}
                    </h3>
                    <v-chip
                      :color="formation.color"
                      size="small"
                      variant="outlined"
                    >
                      {{ formation.duration }}
                    </v-chip>
                  </div>
                </div>
                
                <div class="mb-4">
                  <h4 class="text-h6 font-weight-bold mb-2 text-secondary">
                    Objectif principal
                  </h4>
                  <p class="text-body-1 mb-4">{{ formation.objectifPrincipal }}</p>
                </div>
                
                <div class="mb-4">
                  <h4 class="text-h6 font-weight-bold mb-3 text-secondary">
                    Objectifs spécifiques
                  </h4>
                  <v-list class="bg-transparent pa-0">
                    <v-list-item
                      v-for="objectif in formation.objectifsSpecifiques"
                      :key="objectif"
                      class="pa-0 mb-1"
                      density="compact"
                    >
                      <template v-slot:prepend>
                        <v-icon 
                          icon="mdi-check-circle" 
                          :color="formation.color" 
                          size="16" 
                          class="mr-2"
                        />
                      </template>
                      <v-list-item-title class="text-body-2">
                        {{ objectif }}
                      </v-list-item-title>
                    </v-list-item>
                  </v-list>
                </div>
              </v-card-text>
              
              <v-card-actions class="pa-6 pt-0">
                <v-btn
                  :color="formation.color"
                  variant="flat"
                  class="text-capitalize"
                  block
                  @click="openFormationDialog(formation)"
                >
                  Plus d'informations
                  <v-icon end>mdi-arrow-right</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Certifications ESG-Stratégies Section -->
    <section id="certifications-esg" class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <v-icon icon="mdi-medal" size="64" color="secondary" class="mb-4" />
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Certifications ESG-Stratégies
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Certifications propriétaires développées par nos experts
            </p>
          </v-col>
        </v-row>
        
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card elevation="2" class="pa-8 text-center">
              <v-icon icon="mdi-information" size="48" color="secondary" class="mb-4" />
              <h3 class="text-h5 font-weight-bold mb-4 text-primary">
                Programmes en développement
              </h3>
              <p class="text-body-1 mb-6">
                Nos certifications exclusives ESG-Stratégies sont actuellement en cours d'élaboration. 
                Elles seront conçues pour répondre spécifiquement aux enjeux de durabilité du contexte africain.
              </p>
              <v-btn
                to="/contact"
                color="secondary"
                variant="outlined"
                size="large"
              >
                Être informé du lancement
                <v-icon end>mdi-bell</v-icon>
              </v-btn>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Master Class Section -->
    <section id="master-class" class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <v-icon icon="mdi-school" size="64" color="accent" class="mb-4" />
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Master Class
            </h2>
            <p class="text-h6 text-grey-darken-1">
              Sessions exclusives avec des experts internationaux
            </p>
          </v-col>
        </v-row>
        
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card elevation="2" class="pa-8">
              <div class="text-center mb-6">
                <v-icon icon="mdi-account-tie" size="48" color="accent" class="mb-4" />
                <h3 class="text-h5 font-weight-bold mb-4 text-primary">
                  Sessions d'excellence
                </h3>
              </div>
              <p class="text-body-1 mb-6">
                Nos Master Class sont des sessions intensives animées par des experts reconnus internationalement. 
                Elles offrent une opportunité unique d'approfondir des thématiques ESG stratégiques et d'échanger 
                avec des leaders d'opinion du secteur.
              </p>
              
              <v-divider class="my-6" />
              
              <div class="mb-4">
                <h4 class="text-h6 font-weight-bold mb-3">Caractéristiques :</h4>
                <v-list class="bg-transparent">
                  <v-list-item
                    v-for="caracteristique in masterClassCaracteristiques"
                    :key="caracteristique"
                    class="px-0"
                  >
                    <template v-slot:prepend>
                      <v-icon icon="mdi-check-circle" color="accent" size="20" class="mr-3" />
                    </template>
                    <v-list-item-title>{{ caracteristique }}</v-list-item-title>
                  </v-list-item>
                </v-list>
              </div>
              
              <div class="text-center mt-6">
                <v-btn
                  to="/contact"
                  color="accent"
                  variant="flat"
                  size="large"
                >
                  Demander le calendrier des Master Class
                  <v-icon end>mdi-calendar</v-icon>
                </v-btn>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Avantages Section -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">
              Pourquoi Choisir Nos Formations ?
            </h2>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="avantage in avantages"
            :key="avantage.title"
            cols="12"
            md="6"
            lg="3"
          >
            <div class="text-center">
              <v-icon
                :icon="avantage.icon"
                size="64"
                color="primary"
                class="mb-4"
              />
              <h3 class="text-h6 font-weight-bold mb-3 text-primary">
                {{ avantage.title }}
              </h3>
              <p class="text-body-2">{{ avantage.description }}</p>
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
              Prêt à Former Vos Équipes ?
            </h2>
            <p class="text-h6 mb-8">
              Contactez-nous pour discuter de vos besoins en formation et obtenir un programme sur mesure.
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

    <!-- Formation Dialog -->
    <v-dialog v-model="formationDialog" max-width="900" scrollable>
      <v-card v-if="selectedFormation">
        <v-card-title class="d-flex align-center pa-6">
          <v-icon
            :icon="selectedFormation.icon"
            :color="selectedFormation.color"
            size="32"
            class="mr-3"
          />
          <span class="text-h5">{{ selectedFormation.title }}</span>
          <v-spacer />
          <v-btn
            icon="mdi-close"
            variant="text"
            @click="formationDialog = false"
          />
        </v-card-title>
        
        <v-card-text class="pa-6">
          <div class="mb-6">
            <h4 class="text-h6 font-weight-bold mb-3">Détails de la formation</h4>
            <v-row>
              <v-col cols="12" md="6">
                <div class="d-flex align-center mb-2">
                  <v-icon icon="mdi-clock-outline" size="16" class="mr-2" />
                  <span class="text-body-2"><strong>Durée :</strong> {{ selectedFormation.duration }}</span>
                </div>
                <div class="d-flex align-center mb-2">
                  <v-icon icon="mdi-account-group" size="16" class="mr-2" />
                  <span class="text-body-2"><strong>Participants :</strong> {{ selectedFormation.participants }}</span>
                </div>
              </v-col>
              <v-col cols="12" md="6">
                <div class="d-flex align-center mb-2">
                  <v-icon icon="mdi-map-marker" size="16" class="mr-2" />
                  <span class="text-body-2"><strong>Lieu :</strong> {{ selectedFormation.lieu }}</span>
                </div>
                <div class="d-flex align-center mb-2">
                  <v-icon icon="mdi-certificate" size="16" class="mr-2" />
                  <span class="text-body-2"><strong>Certification :</strong> {{ selectedFormation.certification }}</span>
                </div>
              </v-col>
            </v-row>
          </div>
          
          <div class="mb-6">
            <h4 class="text-h6 font-weight-bold mb-3">Programme détaillé</h4>
            <v-expansion-panels>
              <v-expansion-panel
                v-for="(module, index) in selectedFormation.programme"
                :key="index"
                :title="`Module ${index + 1}: ${module.titre}`"
              >
                <v-expansion-panel-text>
                  <p class="mb-3">{{ module.description }}</p>
                  <ul>
                    <li v-for="point in module.points" :key="point" class="mb-1">
                      {{ point }}
                    </li>
                  </ul>
                </v-expansion-panel-text>
              </v-expansion-panel>
            </v-expansion-panels>
          </div>
        </v-card-text>
        
        <v-card-actions class="pa-6">
          <v-spacer />
          <v-btn
            to="/contact"
            :color="selectedFormation.color"
            variant="flat"
            class="text-capitalize"
          >
            S'inscrire à cette formation
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'Formations',
  data() {
    return {
      formationDialog: false,
      selectedFormation: null,
      
      categoriesFormation: [
        {
          id: 'certifications-internationales',
          title: 'Certifications Internationales',
          description: 'Formations certifiantes conformes aux normes ISO et standards internationaux reconnus',
          icon: 'mdi-certificate',
          color: 'primary'
        },
        {
          id: 'certifications-esg',
          title: 'Certifications ESG-Stratégies',
          description: 'Certifications propriétaires développées par nos experts pour le contexte africain',
          icon: 'mdi-medal',
          color: 'secondary'
        },
        {
          id: 'master-class',
          title: 'Master Class',
          description: 'Sessions exclusives animées par des experts internationaux de haut niveau',
          icon: 'mdi-school',
          color: 'accent'
        }
      ],
      
      masterClassCaracteristiques: [
        'Sessions intensives de 1 à 2 jours',
        'Intervenants experts internationaux',
        'Groupes restreints pour favoriser les échanges',
        'Thématiques ESG stratégiques et d\'actualité',
        'Networking avec des leaders du secteur',
        'Certificat de participation'
      ],
      
      publicCible: [
        {
          title: 'Chefs d\'entreprises',
          icon: 'mdi-account-tie'
        },
        {
          title: 'Responsables RSE/QSE',
          icon: 'mdi-shield-check'
        },
        {
          title: 'Responsables RH et Managers',
          icon: 'mdi-account-group'
        },
        {
          title: 'Responsables Communications',
          icon: 'mdi-bullhorn'
        }
      ],
      
      formations: [
        {
          id: 1,
          title: 'Management de la RSE ISO 26000 et Reporting ESG',
          icon: 'mdi-certificate',
          color: 'primary',
          duration: '5 jours',
          participants: '12-15 personnes',
          lieu: 'Ouagadougou ou sur site',
          certification: 'Certificat de participation',
          objectifPrincipal: 'Aider les managers à mettre en œuvre des démarches RSE cohérentes, efficaces et gagnantes au sein de leur organisation.',
          objectifsSpecifiques: [
            'Maîtriser les concepts et enjeux de la RSE pour son entreprise',
            'Connaître les principes, domaines et exigences de la norme ISO 26000',
            'Intégrer le développement durable dans l\'organisation selon ISO 26000',
            'Évaluer la performance de la stratégie RSE',
            'Valoriser la démarche auprès des parties prenantes'
          ],
          programme: [
            {
              titre: 'Fondamentaux de la RSE',
              description: 'Introduction aux concepts clés de la responsabilité sociétale',
              points: [
                'Définitions et enjeux de la RSE',
                'Contexte réglementaire et normatif',
                'Parties prenantes et matérialité'
              ]
            },
            {
              titre: 'Norme ISO 26000',
              description: 'Étude approfondie de la norme internationale',
              points: [
                'Les 7 questions centrales',
                'Principes de la responsabilité sociétale',
                'Mise en pratique dans l\'organisation'
              ]
            }
          ]
        },
        {
          id: 2,
          title: 'Évaluation et Mesure d\'Impact ESG',
          icon: 'mdi-chart-line',
          color: 'secondary',
          duration: '3 jours',
          participants: '10-12 personnes',
          lieu: 'Ouagadougou ou sur site',
          certification: 'Certificat de participation',
          objectifPrincipal: 'Développer les compétences nécessaires pour évaluer et mesurer l\'impact ESG des activités organisationnelles.',
          objectifsSpecifiques: [
            'Comprendre les méthodologies d\'évaluation ESG',
            'Maîtriser les outils de mesure d\'impact',
            'Développer des indicateurs pertinents',
            'Produire des rapports d\'impact'
          ],
          programme: [
            {
              titre: 'Méthodologies d\'évaluation',
              description: 'Approches et frameworks d\'évaluation ESG',
              points: [
                'Frameworks internationaux',
                'Méthodologies sectorielles',
                'Outils de collecte de données'
              ]
            }
          ]
        },
        {
          id: 3,
          title: 'Étude d\'Impact Environnemental et Social (EIES)',
          icon: 'mdi-earth',
          color: 'primary',
          duration: '7 jours',
          participants: '15-20 personnes',
          lieu: 'Ouagadougou ou sur site',
          certification: 'Certificat professionnel',
          objectifPrincipal: 'Doter les cadres du secteur privé et public en compétences pour conduire une EIES, conseiller les entreprises et mettre en œuvre un PGES.',
          objectifsSpecifiques: [
            'Comprendre le contexte des activités exigeant une EIES',
            'Cerner les enjeux environnementaux, sociaux et économiques',
            'Maîtriser les cadres réglementaire et institutionnel',
            'Conduire et rapporter une étude d\'impact',
            'Mettre en œuvre un Plan de Gestion Environnemental et Social'
          ],
          programme: [
            {
              titre: 'Cadre réglementaire',
              description: 'Contexte légal et institutionnel des EIES',
              points: [
                'Réglementation nationale et internationale',
                'Procédures d\'autorisation',
                'Rôles des institutions'
              ]
            }
          ]
        },
        {
          id: 4,
          title: 'Management Environnemental ISO 14001',
          icon: 'mdi-leaf',
          color: 'primary',
          duration: '4 jours',
          participants: '12-15 personnes',
          lieu: 'Ouagadougou ou sur site',
          certification: 'Certificat de participation',
          objectifPrincipal: 'Aider les managers à mettre en place une démarche SME conforme aux enjeux de l\'entreprise et aux exigences de l\'ISO 14001.',
          objectifsSpecifiques: [
            'Maîtriser les concepts et enjeux environnementaux',
            'Connaître les exigences de la norme ISO 14001',
            'Mettre en place un système de management environnemental',
            'Évaluer la performance et améliorer la démarche SME'
          ],
          programme: [
            {
              titre: 'Système de Management Environnemental',
              description: 'Principes et mise en œuvre d\'un SME',
              points: [
                'Politique environnementale',
                'Planification et objectifs',
                'Mise en œuvre et fonctionnement'
              ]
            }
          ]
        },
        {
          id: 5,
          title: 'Management de la Santé Sécurité au Travail ISO 45001',
          icon: 'mdi-shield-account',
          color: 'accent',
          duration: '4 jours',
          participants: '12-15 personnes',
          lieu: 'Ouagadougou ou sur site',
          certification: 'Certificat de participation',
          objectifPrincipal: 'Aider les managers à mettre en place une démarche SST conforme aux enjeux de l\'entreprise et aux exigences de l\'ISO 45001.',
          objectifsSpecifiques: [
            'Maîtriser les concepts et enjeux de la Santé Sécurité au Travail',
            'Connaître les exigences de la norme ISO 45001',
            'Mettre en place un système de management SST',
            'Évaluer la performance et améliorer la démarche SST'
          ],
          programme: [
            {
              titre: 'Système de Management SST',
              description: 'Principes et mise en œuvre d\'un système SST',
              points: [
                'Politique SST',
                'Identification des dangers',
                'Gestion des risques'
              ]
            }
          ]
        },
        {
          id: 6,
          title: 'Système de Management Intégré QHSE',
          icon: 'mdi-cogs',
          color: 'secondary',
          duration: '6 jours',
          participants: '10-12 personnes',
          lieu: 'Ouagadougou ou sur site',
          certification: 'Certificat professionnel',
          objectifPrincipal: 'Permettre de s\'approprier une méthodologie pour piloter conjointement les trois systèmes qualité, sécurité et environnement en place dans l\'entreprise.',
          objectifsSpecifiques: [
            'Définir les enjeux d\'une gestion intégrée QHSE',
            'Établir le niveau d\'intégration des référentiels',
            'Construire son système de management intégré',
            'Faire vivre efficacement le système avec la bonne méthodologie'
          ],
          programme: [
            {
              titre: 'Intégration des systèmes',
              description: 'Approche intégrée des systèmes QHSE',
              points: [
                'Synergies entre les référentiels',
                'Processus intégrés',
                'Pilotage unifié'
              ]
            }
          ]
        }
      ],
      
      avantages: [
        {
          title: 'Expertise Reconnue',
          description: 'Formateurs experts avec une expérience terrain significative',
          icon: 'mdi-star'
        },
        {
          title: 'Approche Pratique',
          description: 'Formations basées sur des cas concrets et des exercices pratiques',
          icon: 'mdi-tools'
        },
        {
          title: 'Flexibilité',
          description: 'Formations sur mesure adaptées à vos besoins spécifiques',
          icon: 'mdi-puzzle'
        },
        {
          title: 'Suivi Post-Formation',
          description: 'Accompagnement et support après la formation',
          icon: 'mdi-account-check'
        }
      ]
    }
  },
  
  methods: {
    openFormationDialog(formation) {
      this.selectedFormation = formation
      this.formationDialog = true
    },
    
    downloadCatalog() {
      // Simulation du téléchargement du catalogue
      this.$toast.success('Le catalogue sera bientôt disponible en téléchargement.')
    },
    
    scrollToCategory(categoryId) {
      const element = document.getElementById(categoryId)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' })
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

.formation-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.formation-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
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
}
</style>