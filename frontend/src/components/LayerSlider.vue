<template>
  <div class="layer-slider-container">
    <div class="layer-slider" ref="sliderContainer">
      <!-- Slides -->
      <div 
        v-for="(slide, index) in sliderData.slides" 
        :key="slide.id"
        class="layer-slide"
        :class="{ 'active': currentSlide === index }"
        :style="getSlideBackground(slide)"
      >
        <!-- Background Overlay -->
        <div class="slide-overlay" :style="{ background: slide.background.overlay }"></div>
        
        <!-- Slide Content -->
        <v-container class="slide-content-container">
          <v-row class="slide-row" align="center" justify="center">
            <!-- Dynamic Layout based on slide configuration -->
            <template v-if="slide.layout.textPosition === 'left'">
              <!-- Text Content - Left -->
              <v-col 
                cols="12" 
                md="6" 
                :lg="Math.round(slide.layout.contentWidth.replace('%', '') / 100 * 12)"
                class="slide-text-col"
                :class="{ 'order-1': $vuetify.display.mdAndUp, 'order-2': $vuetify.display.smAndDown }"
              >
                <div class="slide-text-content">
                  <!-- Title -->
                  <h1 
                    class="slide-title"
                    :class="`animate-${slide.title.animation}`"
                    :style="getElementStyle(slide.title)"
                    :data-delay="slide.title.delay"
                    :data-duration="slide.title.duration"
                  >
                    {{ slide.title.text }}
                  </h1>
                  
                  <!-- Subtitle -->
                  <h2 
                    class="slide-subtitle"
                    :class="`animate-${slide.subtitle.animation}`"
                    :style="getElementStyle(slide.subtitle)"
                    :data-delay="slide.subtitle.delay"
                    :data-duration="slide.subtitle.duration"
                  >
                    {{ slide.subtitle.text }}
                  </h2>
                  
                  <!-- Description -->
                  <p 
                    class="slide-description"
                    :class="`animate-${slide.description.animation}`"
                    :style="getElementStyle(slide.description)"
                    :data-delay="slide.description.delay"
                    :data-duration="slide.description.duration"
                  >
                    {{ slide.description.text }}
                  </p>
                  
                  <!-- Buttons -->
                  <div class="slide-actions">
                    <v-btn
                      :to="slide.primaryButton.url.startsWith('http') ? undefined : slide.primaryButton.url"
                      :href="slide.primaryButton.url.startsWith('http') ? slide.primaryButton.url : undefined"
                      :target="slide.primaryButton.url.startsWith('http') ? '_blank' : undefined"
                      class="slide-btn-primary"
                      :class="`animate-${slide.primaryButton.animation}`"
                      :style="getElementStyle(slide.primaryButton)"
                      :data-delay="slide.primaryButton.delay"
                      :data-duration="slide.primaryButton.duration"
                      size="large"
                      variant="outlined"
                    >
                      {{ slide.primaryButton.text }}
                    </v-btn>
                    
                    <v-btn
                      :to="slide.secondaryButton.url.startsWith('http') ? undefined : slide.secondaryButton.url"
                      :href="slide.secondaryButton.url.startsWith('http') ? slide.secondaryButton.url : undefined"
                      :target="slide.secondaryButton.url.startsWith('http') ? '_blank' : undefined"
                      class="slide-btn-secondary"
                      :class="`animate-${slide.secondaryButton.animation}`"
                      :style="getElementStyle(slide.secondaryButton)"
                      :data-delay="slide.secondaryButton.delay"
                      :data-duration="slide.secondaryButton.duration"
                      size="large"
                      variant="text"
                    >
                      {{ slide.secondaryButton.text }}
                      <v-icon v-if="slide.secondaryButton.url.startsWith('http')" right>mdi-open-in-new</v-icon>
                    </v-btn>
                  </div>
                </div>
              </v-col>
              
              <!-- Image Content - Right -->
              <v-col 
                cols="12" 
                md="6" 
                :lg="Math.round(slide.layout.imageWidth.replace('%', '') / 100 * 12)"
                class="slide-image-col"
                :class="{ 'order-2': $vuetify.display.mdAndUp, 'order-1': $vuetify.display.smAndDown }"
              >
                <div 
                  class="slide-image-container"
                  :class="`animate-${slide.image.animation}`"
                  :data-delay="slide.image.delay"
                  :data-duration="slide.image.duration"
                >
                  <img
                    :src="slide.image.src"
                    :alt="slide.image.alt"
                    class="slide-image"
                    :style="getElementStyle(slide.image)"
                  />
                </div>
              </v-col>
            </template>
            
            <template v-else>
              <!-- Image Content - Left -->
              <v-col 
                cols="12" 
                md="6" 
                :lg="Math.round(slide.layout.imageWidth.replace('%', '') / 100 * 12)"
                class="slide-image-col"
                :class="{ 'order-1': $vuetify.display.mdAndUp, 'order-1': $vuetify.display.smAndDown }"
              >
                <div 
                  class="slide-image-container"
                  :class="`animate-${slide.image.animation}`"
                  :data-delay="slide.image.delay"
                  :data-duration="slide.image.duration"
                >
                  <img
                    :src="slide.image.src"
                    :alt="slide.image.alt"
                    class="slide-image"
                    :style="getElementStyle(slide.image)"
                  />
                </div>
              </v-col>
              
              <!-- Text Content - Right -->
              <v-col 
                cols="12" 
                md="6" 
                :lg="Math.round(slide.layout.contentWidth.replace('%', '') / 100 * 12)"
                class="slide-text-col"
                :class="{ 'order-2': $vuetify.display.mdAndUp, 'order-2': $vuetify.display.smAndDown }"
              >
                <div class="slide-text-content">
                  <!-- Title -->
                  <h1 
                    class="slide-title"
                    :class="`animate-${slide.title.animation}`"
                    :style="getElementStyle(slide.title)"
                    :data-delay="slide.title.delay"
                    :data-duration="slide.title.duration"
                  >
                    {{ slide.title.text }}
                  </h1>
                  
                  <!-- Subtitle -->
                  <h2 
                    class="slide-subtitle"
                    :class="`animate-${slide.subtitle.animation}`"
                    :style="getElementStyle(slide.subtitle)"
                    :data-delay="slide.subtitle.delay"
                    :data-duration="slide.subtitle.duration"
                  >
                    {{ slide.subtitle.text }}
                  </h2>
                  
                  <!-- Description -->
                  <p 
                    class="slide-description"
                    :class="`animate-${slide.description.animation}`"
                    :style="getElementStyle(slide.description)"
                    :data-delay="slide.description.delay"
                    :data-duration="slide.description.duration"
                  >
                    {{ slide.description.text }}
                  </p>
                  
                  <!-- Buttons -->
                  <div class="slide-actions">
                    <v-btn
                      :to="slide.primaryButton.url.startsWith('http') ? undefined : slide.primaryButton.url"
                      :href="slide.primaryButton.url.startsWith('http') ? slide.primaryButton.url : undefined"
                      :target="slide.primaryButton.url.startsWith('http') ? '_blank' : undefined"
                      class="slide-btn-primary"
                      :class="`animate-${slide.primaryButton.animation}`"
                      :style="getElementStyle(slide.primaryButton)"
                      :data-delay="slide.primaryButton.delay"
                      :data-duration="slide.primaryButton.duration"
                      size="large"
                      variant="outlined"
                    >
                      {{ slide.primaryButton.text }}
                    </v-btn>
                    
                    <v-btn
                      :to="slide.secondaryButton.url.startsWith('http') ? undefined : slide.secondaryButton.url"
                      :href="slide.secondaryButton.url.startsWith('http') ? slide.secondaryButton.url : undefined"
                      :target="slide.secondaryButton.url.startsWith('http') ? '_blank' : undefined"
                      class="slide-btn-secondary"
                      :class="`animate-${slide.secondaryButton.animation}`"
                      :style="getElementStyle(slide.secondaryButton)"
                      :data-delay="slide.secondaryButton.delay"
                      :data-duration="slide.secondaryButton.duration"
                      size="large"
                      variant="text"
                    >
                      {{ slide.secondaryButton.text }}
                      <v-icon v-if="slide.secondaryButton.url.startsWith('http')" right>mdi-open-in-new</v-icon>
                    </v-btn>
                  </div>
                </div>
              </v-col>
            </template>
          </v-row>
        </v-container>
      </div>
      
      <!-- Navigation -->
      <div v-if="sliderData.settings.navigation" class="slider-navigation">
        <button 
          class="nav-btn nav-prev" 
          @click="previousSlide"
          :disabled="!sliderData.settings.loop && currentSlide === 0"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </button>
        <button 
          class="nav-btn nav-next" 
          @click="nextSlide"
          :disabled="!sliderData.settings.loop && currentSlide === sliderData.slides.length - 1"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </button>
      </div>
      
      <!-- Pagination -->
      <div v-if="sliderData.settings.pagination" class="slider-pagination">
        <button
          v-for="(slide, index) in sliderData.slides"
          :key="slide.id"
          class="pagination-dot"
          :class="{ 'active': currentSlide === index }"
          @click="goToSlide(index)"
        ></button>
      </div>
    </div>
  </div>
</template>

<script>
import sliderData from '@/data/slider.json'

export default {
  name: 'LayerSlider',
  data() {
    return {
      sliderData,
      currentSlide: 0,
      autoplayTimer: null,
      isPlaying: true,
      animationTimeout: null
    }
  },
  mounted() {
    this.initSlider()
    this.startAutoplay()
    this.setupKeyboardNavigation()
  },
  beforeUnmount() {
    this.stopAutoplay()
    if (this.animationTimeout) {
      clearTimeout(this.animationTimeout)
    }
  },
  methods: {
    initSlider() {
      // Initialize first slide animations
      this.$nextTick(() => {
        this.triggerSlideAnimations(0)
      })
    },
    
    getSlideBackground(slide) {
      if (slide.background.type === 'gradient') {
        return {
          background: slide.background.value
        }
      }
      return {
        backgroundColor: slide.background.value || '#000'
      }
    },
    
    getElementStyle(element) {
      const style = { ...element.style }
      
      // Convert CSS properties to Vue style object
      Object.keys(style).forEach(key => {
        if (typeof style[key] === 'string' && style[key].includes('clamp')) {
          // Keep clamp values as is
          return
        }
      })
      
      return style
    },
    
    nextSlide() {
      const nextIndex = this.currentSlide + 1
      if (nextIndex >= this.sliderData.slides.length) {
        if (this.sliderData.settings.loop) {
          this.goToSlide(0)
        }
      } else {
        this.goToSlide(nextIndex)
      }
    },
    
    previousSlide() {
      const prevIndex = this.currentSlide - 1
      if (prevIndex < 0) {
        if (this.sliderData.settings.loop) {
          this.goToSlide(this.sliderData.slides.length - 1)
        }
      } else {
        this.goToSlide(prevIndex)
      }
    },
    
    goToSlide(index) {
      if (index === this.currentSlide) return
      
      // Reset animations for current slide
      this.resetSlideAnimations(this.currentSlide)
      
      // Change slide
      this.currentSlide = index
      
      // Trigger animations for new slide
      this.$nextTick(() => {
        this.triggerSlideAnimations(index)
      })
      
      // Restart autoplay
      if (this.isPlaying) {
        this.restartAutoplay()
      }
    },
    
    triggerSlideAnimations(slideIndex) {
      const slide = this.$el.querySelectorAll('.layer-slide')[slideIndex]
      if (!slide) return
      
      const animatedElements = slide.querySelectorAll('[class*="animate-"]')
      
      animatedElements.forEach(element => {
        const delay = parseInt(element.dataset.delay) || 0
        const duration = parseInt(element.dataset.duration) || 600
        
        // Reset animation
        element.style.opacity = '0'
        element.style.transform = this.getInitialTransform(element.className)
        
        // Trigger animation with delay
        setTimeout(() => {
          element.style.transition = `all ${duration}ms cubic-bezier(0.25, 0.46, 0.45, 0.94)`
          element.style.opacity = '1'
          element.style.transform = 'translate3d(0, 0, 0) scale(1) rotate(0deg)'
        }, delay)
      })
    },
    
    resetSlideAnimations(slideIndex) {
      const slide = this.$el.querySelectorAll('.layer-slide')[slideIndex]
      if (!slide) return
      
      const animatedElements = slide.querySelectorAll('[class*="animate-"]')
      animatedElements.forEach(element => {
        element.style.opacity = '0'
        element.style.transform = this.getInitialTransform(element.className)
      })
    },
    
    getInitialTransform(className) {
      if (className.includes('slideInLeft')) return 'translate3d(-100px, 0, 0)'
      if (className.includes('slideInRight')) return 'translate3d(100px, 0, 0)'
      if (className.includes('slideInUp')) return 'translate3d(0, 50px, 0)'
      if (className.includes('slideInDown')) return 'translate3d(0, -50px, 0)'
      if (className.includes('fadeInDown')) return 'translate3d(0, -30px, 0)'
      if (className.includes('fadeInUp')) return 'translate3d(0, 30px, 0)'
      if (className.includes('zoomIn')) return 'scale(0.8)'
      if (className.includes('bounceIn')) return 'scale(0.3)'
      if (className.includes('pulse')) return 'scale(0.95)'
      return 'translate3d(0, 0, 0)'
    },
    
    startAutoplay() {
      if (!this.sliderData.settings.autoplay) return
      
      this.autoplayTimer = setInterval(() => {
        this.nextSlide()
      }, this.sliderData.settings.autoplayDelay)
    },
    
    stopAutoplay() {
      if (this.autoplayTimer) {
        clearInterval(this.autoplayTimer)
        this.autoplayTimer = null
      }
    },
    
    restartAutoplay() {
      this.stopAutoplay()
      this.startAutoplay()
    },
    
    pauseAutoplay() {
      if (this.sliderData.settings.pauseOnHover) {
        this.isPlaying = false
        this.stopAutoplay()
      }
    },
    
    resumeAutoplay() {
      if (this.sliderData.settings.pauseOnHover) {
        this.isPlaying = true
        this.startAutoplay()
      }
    },
    
    setupKeyboardNavigation() {
      if (!this.sliderData.settings.keyboard) return
      
      document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') {
          this.previousSlide()
        } else if (e.key === 'ArrowRight') {
          this.nextSlide()
        }
      })
    }
  }
}
</script>

<style scoped>
.layer-slider-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.layer-slider {
  position: relative;
  width: 100%;
  height: 100%;
}

.layer-slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  visibility: hidden;
  transition: opacity 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  display: flex;
  align-items: center;
  justify-content: center;
}

.layer-slide.active {
  opacity: 1;
  visibility: visible;
  z-index: 2;
}

.slide-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.slide-content-container {
  position: relative;
  z-index: 3;
  height: 100%;
  display: flex;
  align-items: center;
}

.slide-row {
  height: 100%;
  margin: 0;
  display: flex;
  align-items: center;
}

.slide-text-col,
.slide-image-col {
  display: flex;
  align-items: center;
  padding: 2rem 1rem;
}

.slide-text-content {
  width: 100%;
}

.slide-title {
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.slide-subtitle {
  margin-bottom: 2rem;
  line-height: 1.2;
}

.slide-description {
  margin-bottom: 2.5rem;
  line-height: 1.6;
}

.slide-actions {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
  align-items: center;
}

.slide-btn-primary,
.slide-btn-secondary {
  text-transform: none;
  letter-spacing: 0.5px;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.slide-btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

.slide-btn-secondary:hover {
  transform: translateY(-2px);
}

.slide-image-container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slide-image {
  transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.slide-image:hover {
  transform: scale(1.03);
}

/* Navigation */
.slider-navigation {
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  transform: translateY(-50%);
  z-index: 10;
  pointer-events: none;
}

.nav-btn {
  position: absolute;
  width: 60px;
  height: 60px;
  background: rgba(255,255,255,0.2);
  backdrop-filter: blur(15px);
  border: 2px solid rgba(255,255,255,0.4);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  pointer-events: auto;
  color: white;
}

.nav-btn:hover:not(:disabled) {
  background: rgba(255,255,255,0.35);
  border-color: rgba(255,255,255,0.7);
  transform: scale(1.1);
}

.nav-btn:disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.nav-prev {
  left: 30px;
}

.nav-next {
  right: 30px;
}

/* Pagination */
.slider-pagination {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  z-index: 10;
}

.pagination-dot {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: rgba(255,255,255,0.6);
  border: 2px solid rgba(255,255,255,0.9);
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.pagination-dot:hover {
  background: rgba(255,255,255,0.8);
  transform: scale(1.15);
}

.pagination-dot.active {
  background: white;
  transform: scale(1.3);
  box-shadow: 0 0 15px rgba(255,255,255,0.6);
}

/* Responsive Design */
@media (max-width: 960px) {
  .slide-text-col,
  .slide-image-col {
    padding: 1.5rem 1rem;
  }
  
  .slide-actions {
    gap: 1rem;
  }
  
  .nav-btn {
    width: 50px;
    height: 50px;
  }
  
  .nav-prev {
    left: 20px;
  }
  
  .nav-next {
    right: 20px;
  }
}

@media (max-width: 600px) {
  .layer-slider-container {
    height: 100vh;
  }
  
  .slide-text-col,
  .slide-image-col {
    padding: 1rem 0.5rem;
  }
  
  .slide-actions {
    flex-direction: column;
    align-items: stretch;
    gap: 0.8rem;
  }
  
  .nav-btn {
    width: 45px;
    height: 45px;
  }
  
  .pagination-dot {
    width: 12px;
    height: 12px;
  }
}

/* Animation Classes */
[class*="animate-"] {
  opacity: 0;
}

.animate-slideInLeft {
  transform: translate3d(-100px, 0, 0);
}

.animate-slideInRight {
  transform: translate3d(100px, 0, 0);
}

.animate-slideInUp {
  transform: translate3d(0, 50px, 0);
}

.animate-slideInDown {
  transform: translate3d(0, -50px, 0);
}

.animate-fadeInDown {
  transform: translate3d(0, -30px, 0);
}

.animate-fadeInUp {
  transform: translate3d(0, 30px, 0);
}

.animate-zoomIn {
  transform: scale(0.8);
}

.animate-bounceIn {
  transform: scale(0.3);
}

.animate-pulse {
  transform: scale(0.95);
}
</style>