<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="8" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Qui sommes-nous ?
            </h1>
            <p class="text-h5 mb-8">
              ESG Stratégies, cabinet d'expertise spécialisé en développement durable et compétitivité organisationnelle
            </p>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Présentation Section -->
    <section class="py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <div class="text-center mb-12">
              <h2 class="text-h3 font-weight-bold mb-6 text-primary">Présentation</h2>
            </div>
            
            <v-card elevation="2" class="pa-8 mb-8">
              <p class="text-body-1 mb-6">
                L'agence de conseil en stratégie ESG est un cabinet d'expertise spécialisé dans l'analyse des politiques et des performances de durabilité / ESG des organisations. L'agence intervient aide les dirigeants, les managers et leurs équipes à optimiser leurs processus de production et opérer leur transition écologique.
              </p>
              
              <p class="text-body-1 mb-6">
                ESG-stratégies offre ses services aux organisations des principaux secteurs de développement. Ces services particulièrement s'adressent aux entreprises, aux ONG et associations, aux collectivités territoriales et aux administrations publiques en quête d'amélioration de leurs pratiques organisationnelles et d'impacts sociétaux.
              </p>
              
              <p class="text-body-1 mb-6">
                ESG-stratégies accompagne ses clients pour les évaluations environnementales (EIES), la mesure d'impact social (MIS) y compris la mise en place et l'audit des systèmes de management de qualité, de santé sécurité au travail, de l'environnement et des démarches RSE. Les prestations s'étendent aux formations, certifications, labellisation et notations ESG.
              </p>
              
              <p class="text-body-1 font-weight-bold">
                L'agence aide les dirigeants, les managers et leurs équipes à optimiser leurs processus de production et opérer leur transition écologique.
              </p>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Vision Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <div class="text-center mb-12">
              <h2 class="text-h3 font-weight-bold mb-6 text-primary">Vision</h2>
            </div>
            
            <v-card elevation="2" class="pa-8 mb-8">
              <p class="text-h6 text-center text-grey-darken-1">
                [Vision à définir - Contenu à fournir par le client]
              </p>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Mission Section -->
    <section class="py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <div class="text-center mb-12">
              <h2 class="text-h3 font-weight-bold mb-6 text-primary">Mission</h2>
            </div>
            
            <v-card elevation="2" class="pa-8 mb-8">
              <p class="text-h6 text-center text-primary">
                Doter les organisations Africaines de stratégies durabilité à haute valeur ajoutée et cohérentes avec leurs enjeux stratégiques prioritaires afin d'accroitre leurs performances et les bénéfices sociétaux au profit des collectivités territoriales
              </p>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Raisons de nous choisir Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Raisons de nous choisir</h2>
            <p class="text-h6 text-grey-darken-1">
              Trois piliers qui fondent notre excellence
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="raison in raisonsChoisir"
            :key="raison.title"
            cols="12"
            md="4"
          >
            <v-card class="value-card h-100 text-center" elevation="2">
              <v-card-text class="pa-8">
                <v-icon
                  :icon="raison.icon"
                  size="64"
                  :color="raison.color"
                  class="mb-4"
                />
                <h3 class="text-h5 font-weight-bold mb-4 text-primary">
                  {{ raison.title }}
                </h3>
                <p class="text-body-1">{{ raison.description }}</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Bénéfices Section -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Que gagnez-vous avec ESG-STRATEGIES ?</h2>
            <p class="text-h6 text-grey-darken-1">
              Nos équipes de spécialistes proposent une palette de solutions pour
            </p>
          </v-col>
        </v-row>
        
        <v-row justify="center">
          <v-col cols="12" md="10">
            <v-list class="bg-transparent">
              <v-list-item
                v-for="benefice in benefices"
                :key="benefice.text"
                class="mb-4"
              >
                <template v-slot:prepend>
                  <v-icon :icon="benefice.icon" :color="benefice.color" size="40" class="mr-4" />
                </template>
                <v-list-item-title class="text-h6 font-weight-medium">
                  {{ benefice.text }}
                </v-list-item-title>
              </v-list-item>
            </v-list>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Engagements RSE Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <div class="text-center mb-12">
              <h2 class="text-h3 font-weight-bold mb-6 text-primary">Engagements RSE</h2>
            </div>
            
            <v-card elevation="2" class="pa-8">
              <p class="text-body-1 text-center">
                ESG-Stratégies s'engage à pratiquer ce qu'elle prêche en intégrant les principes de développement durable dans ses propres opérations et en démontrant un leadership responsable dans tous les aspects de son activité.
              </p>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Valeurs Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Nos Valeurs</h2>
            <p class="text-h6 text-grey-darken-1">
              Les principes qui guident notre action au quotidien
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="valeur in valeurs"
            :key="valeur.title"
            cols="12"
            md="6"
            lg="3"
          >
            <v-card class="value-card h-100 text-center" elevation="2">
              <v-card-text class="pa-8">
                <v-icon
                  :icon="valeur.icon"
                  size="64"
                  :color="valeur.color"
                  class="mb-4"
                />
                <h3 class="text-h5 font-weight-bold mb-4 text-primary">
                  {{ valeur.title }}
                </h3>
                <p class="text-body-1">{{ valeur.description }}</p>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Témoignages Section -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Témoignages Clients</h2>
            <p class="text-h6 text-grey-darken-1">
              Ce que nos clients disent de notre accompagnement
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="temoignage in temoignages"
            :key="temoignage.nom"
            cols="12"
            md="6"
            lg="4"
          >
            <v-card class="testimonial-card h-100" elevation="2">
              <v-card-text class="pa-6">
                <v-icon icon="mdi-format-quote-open" size="32" color="primary" class="mb-4" />
                <p class="text-body-1 mb-6 font-italic">
                  "{{ temoignage.texte }}"
                </p>
                <div class="d-flex align-center">
                  <v-avatar color="primary" class="mr-3">
                    <span class="text-white font-weight-bold">
                      {{ temoignage.nom.charAt(0) }}
                    </span>
                  </v-avatar>
                  <div>
                    <p class="font-weight-bold mb-0">{{ temoignage.nom }}</p>
                    <p class="text-body-2 text-grey-darken-1 mb-0">
                      {{ temoignage.poste }}, {{ temoignage.entreprise }}
                    </p>
                  </div>
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Équipe Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Notre Équipe</h2>
            <p class="text-h6 text-grey-darken-1">
              Des experts passionnés au service de votre transformation durable
            </p>
          </v-col>
        </v-row>
        
        <v-row justify="center">
          <v-col
            v-for="membre in equipe"
            :key="membre.nom"
            cols="12"
            md="6"
            lg="4"
          >
            <v-card class="team-card text-center" elevation="2">
              <v-card-text class="pa-6">
                <v-avatar size="120" color="primary" class="mb-4">
                  <span class="text-h3 text-white font-weight-bold">
                    {{ membre.nom.split(' ').map(n => n.charAt(0)).join('') }}
                  </span>
                </v-avatar>
                <h3 class="text-h5 font-weight-bold mb-2 text-primary">
                  {{ membre.nom }}
                </h3>
                <p class="text-h6 text-secondary mb-4">{{ membre.poste }}</p>
                <p class="text-body-1 mb-4">{{ membre.description }}</p>
                
                <div class="d-flex justify-center">
                  <v-btn
                    v-for="competence in membre.competences"
                    :key="competence"
                    variant="outlined"
                    size="small"
                    color="primary"
                    class="ma-1"
                    disabled
                  >
                    {{ competence }}
                  </v-btn>
                </div>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Statistiques Section -->
    <section class="py-16">
      <v-container>
        <v-row>
          <v-col cols="12" class="text-center mb-12">
            <h2 class="text-h3 font-weight-bold mb-4 text-primary">Nos Réalisations</h2>
            <p class="text-h6 text-grey-darken-1">
              Quelques chiffres qui témoignent de notre impact
            </p>
          </v-col>
        </v-row>
        
        <v-row>
          <v-col
            v-for="stat in statistiques"
            :key="stat.label"
            cols="12"
            md="6"
            lg="3"
            class="text-center"
          >
            <div class="stat-item">
              <v-icon
                :icon="stat.icon"
                size="48"
                :color="stat.color"
                class="mb-4"
              />
              <h3 class="text-h2 font-weight-bold mb-2" :class="`text-${stat.color}`">
                {{ stat.value }}
              </h3>
              <p class="text-h6 text-grey-darken-1">{{ stat.label }}</p>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Contact CTA Section -->
    <section class="py-16 bg-primary">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8" class="text-center text-white">
            <h2 class="text-h3 font-weight-bold mb-6">
              Travaillons Ensemble
            </h2>
            <p class="text-h6 mb-8">
              Vous souhaitez en savoir plus sur notre approche ou discuter de vos besoins ? 
              Contactez-nous pour une consultation personnalisée.
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
                Nous contacter
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
              <v-btn
                href="https://esg-strategies.com/blog/"
                target="_blank"
                color="white"
                variant="text"
                size="large"
                class="text-capitalize"
              >
                <v-icon left>mdi-web</v-icon>
                Notre blog
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
  name: 'About',
  data() {
    return {
      raisonsChoisir: [
        {
          title: 'Notre expertise',
          description: 'Parce que vous écouter et répondre à vos attentes est notre raison d\'être',
          icon: 'mdi-account-star',
          color: 'primary'
        },
        {
          title: 'Notre Simplicité',
          description: 'Car nos solutions accessibles et faciles d\'utilisation garantissent votre satisfaction',
          icon: 'mdi-hand-heart',
          color: 'secondary'
        },
        {
          title: 'Notre Excellence',
          description: 'Car nous associons engagement, énergie et célérité pour atteindre vos objectifs',
          icon: 'mdi-star-circle',
          color: 'accent'
        }
      ],
      
      benefices: [
        {
          text: 'Développer votre attractivité et votre positionnement sur les enjeux ESG stratégiques',
          icon: 'mdi-chart-line-variant',
          color: 'primary'
        },
        {
          text: 'Donner du sens à vos missions et engager votre collaborateurs partenaires',
          icon: 'mdi-account-group',
          color: 'secondary'
        },
        {
          text: 'Améliorer la compétitivité et la performance de votre organisation',
          icon: 'mdi-trophy',
          color: 'accent'
        }
      ],
      
      valeurs: [
        {
          title: 'Excellence',
          description: 'Nous nous engageons à fournir des services de la plus haute qualité, basés sur les meilleures pratiques internationales.',
          icon: 'mdi-star',
          color: 'primary'
        },
        {
          title: 'Innovation',
          description: 'Nous développons des solutions créatives et adaptées aux défis spécifiques de chaque organisation.',
          icon: 'mdi-lightbulb',
          color: 'secondary'
        },
        {
          title: 'Intégrité',
          description: 'Nous agissons avec transparence et éthique dans toutes nos relations professionnelles.',
          icon: 'mdi-shield-check',
          color: 'accent'
        },
        {
          title: 'Durabilité',
          description: 'Nous plaçons le développement durable au cœur de notre mission et de nos recommandations.',
          icon: 'mdi-leaf',
          color: 'neutral'
        }
      ],
      
      temoignages: [
        {
          nom: 'Marie Ouédraogo',
          poste: 'Directrice RSE',
          entreprise: 'Groupe Industriel BF',
          texte: 'ESG Stratégies nous a accompagnés dans la mise en place de notre stratégie RSE. Leur expertise et leur approche pragmatique ont été déterminantes pour notre réussite.'
        },
        {
          nom: 'Jean-Baptiste Kaboré',
          poste: 'Maire',
          entreprise: 'Commune de Ouagadougou',
          texte: 'Grâce à ESG Stratégies, nous avons pu développer un plan de développement durable pour notre commune. Leur accompagnement a été précieux.'
        },
        {
          nom: 'Fatou Traoré',
          poste: 'Coordinatrice',
          entreprise: 'ONG Environnement Sahel',
          texte: 'L\'équipe d\'ESG Stratégies a su comprendre nos enjeux et nous proposer des solutions adaptées à notre contexte. Un partenariat très enrichissant.'
        }
      ],
      
      equipe: [
        {
          nom: 'Dr. Amadou Sankara',
          poste: 'Directeur Général',
          description: 'Expert en développement durable avec plus de 15 ans d\'expérience dans l\'accompagnement des organisations.',
          competences: ['Stratégie ESG', 'Gouvernance', 'Leadership']
        },
        {
          nom: 'Aïcha Compaoré',
          poste: 'Consultante Senior Environnement',
          description: 'Spécialisée en gestion des ressources naturelles et évaluation d\'impact environnemental.',
          competences: ['Environnement', 'Ressources', 'Impact']
        },
        {
          nom: 'Ibrahim Ouattara',
          poste: 'Consultant Social',
          description: 'Expert en responsabilité sociale et engagement communautaire, formateur certifié.',
          competences: ['Social', 'Formation', 'Communauté']
        }
      ],
      
      statistiques: [
        {
          value: '10+',
          label: 'Années d\'expérience',
          icon: 'mdi-calendar-clock',
          color: 'primary'
        },
        {
          value: '150+',
          label: 'Projets réalisés',
          icon: 'mdi-briefcase-check',
          color: 'secondary'
        },
        {
          value: '50+',
          label: 'Organisations accompagnées',
          icon: 'mdi-domain',
          color: 'accent'
        },
        {
          value: '100%',
          label: 'Satisfaction client',
          icon: 'mdi-heart',
          color: 'neutral'
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

.value-card {
  transition: transform 0.3s ease;
}

.value-card:hover {
  transform: translateY(-5px);
}

.testimonial-card {
  transition: transform 0.3s ease;
}

.testimonial-card:hover {
  transform: translateY(-5px);
}

.team-card {
  transition: transform 0.3s ease;
}

.team-card:hover {
  transform: translateY(-5px);
}

.stat-item {
  padding: 2rem 1rem;
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