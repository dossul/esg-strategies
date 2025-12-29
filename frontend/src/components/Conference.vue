<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="10" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Africa Sustainability and Business Intelligence Conference
            </h1>
            <p class="text-h5 mb-4">
              (ASBIC)
            </p>
            <p class="text-h6 mb-8">
              Conférence panafricaine dédiée à la durabilité, à la performance ESG et à l'intelligence stratégique
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
            <v-card elevation="2" class="pa-8 mb-8">
              <h2 class="text-h4 font-weight-bold mb-6 text-primary text-center">
                À propos de l'ASBIC
              </h2>
              <p class="text-body-1 mb-6">
                L'Africa Sustainability and Business Intelligence Conference se distingue par une approche intégrée combinant :
              </p>
              
              <v-list class="bg-transparent">
                <v-list-item class="mb-3">
                  <template v-slot:prepend>
                    <v-icon icon="mdi-leaf" color="primary" size="32" class="mr-4" />
                  </template>
                  <v-list-item-title class="text-h6">
                    Sustainability & ESG
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-body-2 mt-2">
                    RSE, finance durable, ODD, normes internationales
                  </v-list-item-subtitle>
                </v-list-item>
                
                <v-list-item class="mb-3">
                  <template v-slot:prepend>
                    <v-icon icon="mdi-chart-line" color="secondary" size="32" class="mr-4" />
                  </template>
                  <v-list-item-title class="text-h6">
                    Business Intelligence & data stratégique
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-body-2 mt-2">
                    Pilotage de la performance, gestion des risques, aide à la décision
                  </v-list-item-subtitle>
                </v-list-item>
                
                <v-list-item class="mb-3">
                  <template v-slot:prepend>
                    <v-icon icon="mdi-domain" color="accent" size="32" class="mr-4" />
                  </template>
                  <v-list-item-title class="text-h6">
                    Approche sectorielle
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-body-2 mt-2">
                    Mines, énergie, finance, BTP, agro-industrie, PME
                  </v-list-item-subtitle>
                </v-list-item>
              </v-list>
              
              <p class="text-body-1 mt-6">
                L'événement constitue une plateforme stratégique d'échanges, de networking et de montée en compétences, 
                favorisant le dialogue entre entreprises, investisseurs, institutions financières, autorités publiques 
                et partenaires techniques.
              </p>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Pourquoi devenir partenaire Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <h2 class="text-h3 font-weight-bold mb-8 text-primary text-center">
              Pourquoi devenir partenaire ou sponsor ?
            </h2>
            
            <v-card elevation="2" class="pa-8 mb-6">
              <p class="text-body-1 mb-6">
                L'Africa Sustainability and Business Intelligence Conference offre aux partenaires et sponsors une 
                plateforme stratégique de visibilité, d'influence et de networking auprès de décideurs économiques, 
                financiers et institutionnels à l'échelle africaine.
              </p>
              
              <h3 class="text-h5 font-weight-bold mb-4 text-secondary">
                S'associer à l'événement, c'est :
              </h3>
              
              <v-row>
                <v-col
                  v-for="avantage in avantagesPartenariat"
                  :key="avantage.text"
                  cols="12"
                  md="6"
                >
                  <div class="d-flex align-start mb-4">
                    <v-icon
                      :icon="avantage.icon"
                      :color="avantage.color"
                      size="32"
                      class="mr-4 mt-1"
                    />
                    <div>
                      <p class="text-body-1 font-weight-medium">
                        {{ avantage.text }}
                      </p>
                    </div>
                  </div>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Contact Section -->
    <section class="py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card elevation="3" class="pa-8">
              <h2 class="text-h4 font-weight-bold mb-6 text-primary text-center">
                Plus d'informations
              </h2>
              
              <v-list class="bg-transparent">
                <v-list-item>
                  <template v-slot:prepend>
                    <v-icon icon="mdi-web" color="primary" size="32" class="mr-4" />
                  </template>
                  <v-list-item-title class="text-h6">
                    Site web de l'événement
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-body-2 mt-2">
                    [URL à fournir par le client]
                  </v-list-item-subtitle>
                </v-list-item>
                
                <v-divider class="my-4" />
                
                <v-list-item>
                  <template v-slot:prepend>
                    <v-icon icon="mdi-phone" color="secondary" size="32" class="mr-4" />
                  </template>
                  <v-list-item-title class="text-h6">
                    Téléphone
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-body-2 mt-2">
                    [Numéro à fournir par le client]
                  </v-list-item-subtitle>
                </v-list-item>
                
                <v-divider class="my-4" />
                
                <v-list-item>
                  <template v-slot:prepend>
                    <v-icon icon="mdi-email" color="accent" size="32" class="mr-4" />
                  </template>
                  <v-list-item-title class="text-h6">
                    E-mail
                  </v-list-item-title>
                  <v-list-item-subtitle class="text-body-2 mt-2">
                    [Email à fournir par le client]
                  </v-list-item-subtitle>
                </v-list-item>
              </v-list>
              
              <div class="text-center mt-8">
                <v-btn
                  to="/contact"
                  color="primary"
                  variant="flat"
                  size="large"
                  class="text-capitalize"
                >
                  <v-icon left>mdi-email</v-icon>
                  Nous contacter
                </v-btn>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </section>
  </div>
</template>

<script>
export default {
  name: 'Conference',
  data() {
    return {
      avantagesPartenariat: [
        {
          text: 'Valoriser son engagement en faveur de la durabilité et de la performance ESG',
          icon: 'mdi-star',
          color: 'primary'
        },
        {
          text: 'Accroître sa visibilité auprès de dirigeants d\'entreprises, investisseurs et institutions financières',
          icon: 'mdi-eye',
          color: 'secondary'
        },
        {
          text: 'Positionner sa marque comme acteur clé de la transformation durable en Afrique',
          icon: 'mdi-trophy',
          color: 'accent'
        },
        {
          text: 'Accéder à un réseau qualifié de décideurs et d\'experts sectoriels',
          icon: 'mdi-account-group',
          color: 'primary'
        },
        {
          text: 'Contribuer activement aux réflexions stratégiques sur l\'avenir économique du continent',
          icon: 'mdi-lightbulb',
          color: 'secondary'
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

/* Responsive */
@media (max-width: 768px) {
  .display-1 {
    font-size: 2rem !important;
  }
  
  .text-h3 {
    font-size: 1.75rem !important;
  }
}
</style>