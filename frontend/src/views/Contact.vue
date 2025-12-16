<template>
  <div>
    <!-- Hero Section -->
    <section class="hero-section bg-primary">
      <v-container>
        <v-row align="center" class="fill-height">
          <v-col cols="12" md="8" class="text-white">
            <h1 class="display-1 font-weight-bold mb-6">
              Contactez-nous
            </h1>
            <p class="text-h5 mb-8">
              Prêts à vous accompagner dans votre démarche ESG
            </p>
            <v-btn
              href="#contact-form"
              color="white"
              variant="outlined"
              size="large"
              class="text-capitalize"
            >
              <v-icon left>mdi-email</v-icon>
              Nous écrire
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Contact Form Section -->
    <section class="py-16">
      <v-container>
        <v-row>
          <!-- Contact Form -->
          <v-col cols="12" md="8">
            <v-card elevation="3" class="pa-8">
              <h2 class="text-h4 font-weight-bold mb-6 text-neutral">
                Demande de Contact
              </h2>
              
              <v-form ref="contactForm" v-model="formValid" @submit.prevent="submitForm">
                <v-row>
                  <v-col cols="12" md="6">
                    <v-text-field
                      v-model="form.firstName"
                      label="Prénom *"
                      :rules="nameRules"
                      variant="outlined"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="6">
                    <v-text-field
                      v-model="form.lastName"
                      label="Nom *"
                      :rules="nameRules"
                      variant="outlined"
                      required
                    ></v-text-field>
                  </v-col>
                </v-row>
                
                <v-row>
                  <v-col cols="12" md="6">
                    <v-text-field
                      v-model="form.email"
                      label="Email *"
                      :rules="emailRules"
                      variant="outlined"
                      type="email"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="6">
                    <v-text-field
                      v-model="form.phone"
                      label="Téléphone"
                      variant="outlined"
                      type="tel"
                    ></v-text-field>
                  </v-col>
                </v-row>
                
                <v-row>
                  <v-col cols="12" md="6">
                    <v-text-field
                      v-model="form.company"
                      label="Entreprise *"
                      :rules="requiredRules"
                      variant="outlined"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="6">
                    <v-select
                      v-model="form.service"
                      :items="serviceOptions"
                      label="Service d'intérêt *"
                      :rules="requiredRules"
                      variant="outlined"
                      required
                    ></v-select>
                  </v-col>
                </v-row>
                
                <v-row>
                  <v-col cols="12">
                    <v-select
                      v-model="form.budget"
                      :items="budgetOptions"
                      label="Budget estimé"
                      variant="outlined"
                    ></v-select>
                  </v-col>
                </v-row>
                
                <v-row>
                  <v-col cols="12">
                    <v-textarea
                      v-model="form.message"
                      label="Message *"
                      :rules="messageRules"
                      variant="outlined"
                      rows="5"
                      required
                      placeholder="Décrivez votre projet, vos besoins ou vos questions..."
                    ></v-textarea>
                  </v-col>
                </v-row>
                
                <v-row>
                  <v-col cols="12">
                    <v-checkbox
                      v-model="form.consent"
                      :rules="consentRules"
                      required
                    >
                      <template v-slot:label>
                        <span class="text-body-2">
                          J'accepte que mes données soient utilisées pour me recontacter concernant ma demande *
                        </span>
                      </template>
                    </v-checkbox>
                  </v-col>
                </v-row>
                
                <v-row>
                  <v-col cols="12">
                    <v-btn
                      type="submit"
                      color="primary"
                      size="large"
                      variant="flat"
                      class="text-none"
                      :disabled="!formValid"
                      :loading="submitting"
                      block
                    >
                      Envoyer ma demande
                      <v-icon end>mdi-send</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
              </v-form>
            </v-card>
          </v-col>
          
          <!-- Contact Info -->
          <v-col cols="12" md="4">
            <div class="contact-info">
              <!-- Contact Details -->
              <v-card elevation="3" class="mb-6">
                <v-card-text class="pa-6">
                  <h3 class="text-h5 font-weight-bold mb-4 text-neutral">
                    Nos Coordonnées
                  </h3>
                  
                  <div class="contact-item mb-4">
                    <div class="d-flex align-center mb-2">
                      <v-icon color="primary" class="mr-3">mdi-map-marker</v-icon>
                      <span class="font-weight-medium">Adresse</span>
                    </div>
                    <p class="text-body-2 text-grey-darken-1 ml-9">
                      Ouagadougou<br>
                      Burkina Faso
                    </p>
                  </div>
                  
                  <div class="contact-item mb-4">
                    <div class="d-flex align-center mb-2">
                      <v-icon color="primary" class="mr-3">mdi-phone</v-icon>
                      <span class="font-weight-medium">Téléphone</span>
                    </div>
                    <p class="text-body-2 text-grey-darken-1 ml-9">
                      <a href="tel:+22625123456" class="text-decoration-none text-primary">
                        +226 25 12 34 56
                      </a><br>
                      <a href="tel:+22670123456" class="text-decoration-none text-primary">
                        +226 70 12 34 56
                      </a>
                    </p>
                  </div>
                  
                  <div class="contact-item mb-4">
                    <div class="d-flex align-center mb-2">
                      <v-icon color="primary" class="mr-3">mdi-email</v-icon>
                      <span class="font-weight-medium">Email</span>
                    </div>
                    <p class="text-body-2 text-grey-darken-1 ml-9">
                      <a href="mailto:info@esg-strategies.com" class="text-decoration-none text-primary">
                        info@esg-strategies.com
                      </a>
                    </p>
                  </div>
                  
                  <div class="contact-item">
                    <div class="d-flex align-center mb-2">
                      <v-icon color="primary" class="mr-3">mdi-clock</v-icon>
                      <span class="font-weight-medium">Horaires</span>
                    </div>
                    <p class="text-body-2 text-grey-darken-1 ml-9">
                      Lun - Ven : 9h00 - 18h00<br>
                      Sam : 9h00 - 12h00
                    </p>
                  </div>
                </v-card-text>
              </v-card>
              
              <!-- Quick Actions -->
              <v-card elevation="3" class="mb-6">
                <v-card-text class="pa-6">
                  <h3 class="text-h5 font-weight-bold mb-4 text-neutral">
                    Actions Rapides
                  </h3>
                  
                  <v-btn
                    href="tel:+22625123456"
                    color="primary"
                    variant="flat"
                    class="text-none mb-3"
                    block
                  >
                    <v-icon start>mdi-phone</v-icon>
                    Appeler maintenant
                  </v-btn>
                  
                  <v-btn
                    href="mailto:info@esg-strategies.com"
                    color="secondary"
                    variant="outlined"
                    class="text-none mb-3"
                    block
                  >
                    <v-icon start>mdi-email</v-icon>
                    Envoyer un email
                  </v-btn>
                  
                  <v-btn
                    href="#"
                    color="accent"
                    variant="outlined"
                    class="text-none"
                    block
                  >
                    <v-icon start>mdi-calendar</v-icon>
                    Prendre RDV
                  </v-btn>
                </v-card-text>
              </v-card>
              
              <!-- Social Media -->
              <v-card elevation="3">
                <v-card-text class="pa-6">
                  <h3 class="text-h5 font-weight-bold mb-4 text-neutral">
                    Suivez-nous
                  </h3>
                  
                  <div class="d-flex justify-space-around">
                    <v-btn
                      v-for="social in socialMedia"
                      :key="social.name"
                      :href="social.url"
                      :icon="social.icon"
                      :color="social.color"
                      variant="outlined"
                      size="large"
                      target="_blank"
                    ></v-btn>
                  </div>
                </v-card-text>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-container>
    </section>

    <!-- Map Section -->
    <section class="py-16 bg-grey-lighten-5">
      <v-container>
        <div class="text-center mb-8">
          <h2 class="text-h3 font-weight-bold mb-4 text-neutral">
            Notre Localisation
          </h2>
          <p class="text-h6 text-grey-darken-1">
            Venez nous rencontrer dans nos bureaux parisiens
          </p>
        </div>
        
        <!-- Placeholder for map -->
        <v-card elevation="3" height="400" class="d-flex align-center justify-center">
          <div class="text-center">
            <v-icon size="64" color="grey-lighten-1" class="mb-4">mdi-map</v-icon>
            <p class="text-h6 text-grey-darken-1">
              Carte interactive à intégrer
            </p>
            <p class="text-body-2 text-grey-darken-1">
              Ouagadougou, Burkina Faso
            </p>
          </div>
        </v-card>
      </v-container>
    </section>

    <!-- Success Dialog -->
    <v-dialog v-model="showSuccess" max-width="500">
      <v-card>
        <v-card-text class="pa-8 text-center">
          <v-icon size="64" color="success" class="mb-4">mdi-check-circle</v-icon>
          <h3 class="text-h5 font-weight-bold mb-4">Message envoyé !</h3>
          <p class="text-body-1 mb-4">
            Merci pour votre message. Nous vous recontacterons dans les plus brefs délais.
          </p>
          <v-btn color="primary" variant="flat" @click="showSuccess = false">
            Fermer
          </v-btn>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: 'Contact',
  data() {
    return {
      formValid: false,
      submitting: false,
      showSuccess: false,
      form: {
        firstName: '',
        lastName: '',
        email: '',
        phone: '',
        company: '',
        service: '',
        budget: '',
        message: '',
        consent: false
      },
      serviceOptions: [
        'Conseil Environnemental',
        'Responsabilité Sociale',
        'Gouvernance d\'Entreprise',
        'Audit ESG',
        'Formation ESG',
        'Reporting ESG',
        'Due Diligence',
        'Certification',
        'Autre'
      ],
      budgetOptions: [
        'Moins de 10 000€',
        '10 000€ - 25 000€',
        '25 000€ - 50 000€',
        '50 000€ - 100 000€',
        'Plus de 100 000€',
        'À définir'
      ],
      contactInfo: [
        {
          id: 1,
          title: 'Téléphone',
          icon: 'mdi-phone',
          color: 'primary',
          type: 'phone',
          value1: '+226 25 12 34 56',
          value2: '+226 70 12 34 56'
        },
        {
          id: 2,
          title: 'Email',
          icon: 'mdi-email',
          color: 'secondary',
          type: 'email',
          value1: 'info@esg-strategies.com'
        },
        {
          id: 3,
          title: 'Adresse',
          icon: 'mdi-map-marker',
          color: 'accent',
          type: 'address',
          value1: 'Ouagadougou',
          value2: 'Burkina Faso'
        },
        {
          id: 4,
          title: 'Horaires',
          icon: 'mdi-clock',
          color: 'primary',
          type: 'hours',
          value1: 'Lun-Ven: 8h-17h',
          value2: 'Sam: 8h-12h'
        }
      ],
      socialMedia: [
        {
          name: 'LinkedIn',
          icon: 'mdi-linkedin',
          url: '#',
          color: 'blue-darken-3'
        },
        {
          name: 'Twitter',
          icon: 'mdi-twitter',
          url: '#',
          color: 'blue'
        },
        {
          name: 'Facebook',
          icon: 'mdi-facebook',
          url: '#',
          color: 'blue-darken-4'
        },
        {
          name: 'YouTube',
          icon: 'mdi-youtube',
          url: '#',
          color: 'red'
        }
      ],
      nameRules: [
        v => !!v || 'Ce champ est requis',
        v => (v && v.length >= 2) || 'Minimum 2 caractères'
      ],
      emailRules: [
        v => !!v || 'Email requis',
        v => /.+@.+\..+/.test(v) || 'Email invalide'
      ],
      requiredRules: [
        v => !!v || 'Ce champ est requis'
      ],
      messageRules: [
        v => !!v || 'Message requis',
        v => (v && v.length >= 10) || 'Minimum 10 caractères'
      ],
      consentRules: [
        v => !!v || 'Vous devez accepter le traitement de vos données'
      ]
    }
  },
  methods: {
    async submitForm() {
      if (!this.formValid) return
      
      this.submitting = true
      
      try {
        // Simulate form submission
        await new Promise(resolve => setTimeout(resolve, 2000))
        
        // Reset form
        this.$refs.contactForm.reset()
        this.showSuccess = true
        
      } catch (error) {
        console.error('Erreur lors de l\'envoi:', error)
      } finally {
        this.submitting = false
      }
    }
  }
}
</script>

<style scoped>
.page-header {
  background: linear-gradient(135deg, #E53935 0%, #C62828 100%);
}

.contact-info {
  position: sticky;
  top: 2rem;
}

.contact-item {
  border-bottom: 1px solid #f5f5f5;
  padding-bottom: 1rem;
}

.contact-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

@media (max-width: 960px) {
  .contact-info {
    position: static;
  }
}
</style>