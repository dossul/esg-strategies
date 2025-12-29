<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="8" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Nos Partenaires
            </h1>
            <p class="text-h5 mb-8">
              Ensemble pour un avenir durable et responsable
            </p>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Partenaires Section -->
    <section class="py-16">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="10">
            <div class="text-center mb-12">
              <h2 class="text-h3 font-weight-bold mb-6 text-primary">
                Ils nous font confiance
              </h2>
              <p class="text-h6 text-grey-darken-1">
                Des partenaires engagés dans la transformation durable
              </p>
            </div>
            
            <v-row>
              <v-col
                v-for="partenaire in partenaires"
                :key="partenaire.name"
                cols="6"
                sm="4"
                md="3"
                class="d-flex align-center justify-center"
              >
                <v-card
                  class="partner-card pa-6"
                  elevation="2"
                  hover
                  height="150"
                >
                  <div class="d-flex align-center justify-center h-100">
                    <div class="text-center">
                      <v-icon
                        :icon="partenaire.icon"
                        :color="partenaire.color"
                        size="48"
                        class="mb-3"
                      />
                      <h3 class="text-h6 font-weight-bold text-primary">
                        {{ partenaire.name }}
                      </h3>
                      <p class="text-body-2 text-grey-darken-1 mt-2">
                        {{ partenaire.secteur }}
                      </p>
                    </div>
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Devenir Partenaire Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <v-row justify="center">
          <v-col cols="12" md="8">
            <v-card elevation="3" class="pa-8">
              <div class="text-center mb-6">
                <v-icon icon="mdi-handshake" size="64" color="primary" class="mb-4" />
                <h2 class="text-h3 font-weight-bold mb-4 text-primary">
                  Devenez Partenaire
                </h2>
                <p class="text-h6 text-grey-darken-1 mb-6">
                  Rejoignez notre réseau de partenaires engagés pour la durabilité
                </p>
              </div>
              
              <v-divider class="my-6" />
              
              <div class="mb-6">
                <h3 class="text-h5 font-weight-bold mb-4 text-secondary">
                  Avantages du partenariat :
                </h3>
                <v-list class="bg-transparent">
                  <v-list-item
                    v-for="avantage in avantagesPartenariat"
                    :key="avantage"
                    class="px-0 mb-2"
                  >
                    <template v-slot:prepend>
                      <v-icon icon="mdi-check-circle" color="primary" size="24" class="mr-3" />
                    </template>
                    <v-list-item-title class="text-body-1">
                      {{ avantage }}
                    </v-list-item-title>
                  </v-list-item>
                </v-list>
              </div>
              
              <div class="text-center mt-8">
                <v-btn
                  to="/contact"
                  color="primary"
                  variant="flat"
                  size="large"
                  class="text-capitalize"
                >
                  <v-icon left>mdi-email</v-icon>
                  Devenir partenaire
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
  name: 'Partner',
  data() {
    return {
      partenaires: [
        {
          name: 'TECO2',
          secteur: 'Environnement',
          icon: 'mdi-leaf',
          color: 'green'
        },
        {
          name: 'SOMISA',
          secteur: 'Services',
          icon: 'mdi-domain',
          color: 'blue'
        },
        {
          name: 'Coris Bank',
          secteur: 'Finance',
          icon: 'mdi-bank',
          color: 'orange'
        },
        {
          name: 'Sirac',
          secteur: 'Industrie',
          icon: 'mdi-factory',
          color: 'purple'
        },
        {
          name: 'Mam Diet',
          secteur: 'Agroalimentaire',
          icon: 'mdi-food',
          color: 'red'
        },
        {
          name: 'Lateco',
          secteur: 'Construction',
          icon: 'mdi-hammer-wrench',
          color: 'teal'
        },
        {
          name: 'Lauréat-finance',
          secteur: 'Finance',
          icon: 'mdi-currency-usd',
          color: 'indigo'
        },
        {
          name: 'Doris Garden',
          secteur: 'Horticulture',
          icon: 'mdi-flower',
          color: 'pink'
        }
      ],
      
      avantagesPartenariat: [
        'Visibilité accrue auprès d\'un réseau de professionnels ESG',
        'Participation à des événements exclusifs',
        'Accès à notre expertise en développement durable',
        'Opportunités de collaboration sur des projets innovants',
        'Communication sur vos initiatives durables',
        'Networking avec des décideurs et experts'
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

.partner-card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  width: 100%;
}

.partner-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.15) !important;
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