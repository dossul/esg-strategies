<template>
  <div class="hero-slider" @mouseenter="handleMouseEnter" @mouseleave="handleMouseLeave">
    <div class="slider-container">
      <!-- Slides -->
      <div 
        v-for="(slide, index) in sliderData.slides" 
        :key="slide.id"
        class="slide"
        :class="{ active: currentSlide === index }"
        :style="getSlideBackground(slide)"
      >
        <div class="slide-overlay" :style="{ background: slide.background.overlay }"></div>
        <div class="slide-content" :style="getLayoutStyle(slide.layout)">
          <div class="content-wrapper">
            <h1 
              class="slide-title"
              :style="slide.title.style"
              :class="`animate__animated animate__${slide.title.animation}`"
            >
              {{ slide.title.text }}
            </h1>
            <h2 
              class="slide-subtitle"
              :style="slide.subtitle.style"
              :class="`animate__animated animate__${slide.subtitle.animation}`"
            >
              {{ slide.subtitle.text }}
            </h2>
            <p 
              class="slide-description"
              :style="slide.description.style"
              :class="`animate__animated animate__${slide.description.animation}`"
            >
              {{ slide.description.text }}
            </p>
            <div class="slide-buttons">
              <v-btn 
                class="primary-btn"
                :style="slide.primaryButton.style"
                :class="`animate__animated animate__${slide.primaryButton.animation}`"
                size="large"
                :href="slide.primaryButton.url"
              >
                {{ slide.primaryButton.text }}
              </v-btn>
              <v-btn 
                class="secondary-btn"
                :style="slide.secondaryButton.style"
                :class="`animate__animated animate__${slide.secondaryButton.animation}`"
                variant="outlined"
                size="large"
                :href="slide.secondaryButton.url"
              >
                {{ slide.secondaryButton.text }}
              </v-btn>
            </div>
          </div>
          
        </div>
      </div>

      <!-- Navigation Dots -->
      <div v-if="sliderData.settings.pagination" class="slider-dots">
        <button
          v-for="(slide, index) in sliderData.slides"
          :key="`dot-${index}`"
          class="dot"
          :class="{ active: currentSlide === index }"
          @click="goToSlide(index)"
        ></button>
      </div>

      <!-- Navigation Arrows -->
      <div v-if="sliderData.settings.navigation" class="navigation-arrows">
        <button class="nav-arrow prev" @click="prevSlide">
          <v-icon>mdi-chevron-left</v-icon>
        </button>
        <button class="nav-arrow next" @click="nextSlide">
          <v-icon>mdi-chevron-right</v-icon>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import sliderData from '@/data/slider.json'

export default {
  name: 'HeroSlider',
  data() {
    return {
      currentSlide: 0,
      autoplayInterval: null,
      sliderData: sliderData
    }
  },
  mounted() {
    if (this.sliderData.settings.autoplay) {
      this.startAutoplay()
    }
    this.addAnimateCSS()
  },
  beforeUnmount() {
    this.stopAutoplay()
  },
  methods: {
    addAnimateCSS() {
      // Add Animate.css for animations
      if (!document.querySelector('link[href*="animate.css"]')) {
        const link = document.createElement('link')
        link.rel = 'stylesheet'
        link.href = 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css'
        document.head.appendChild(link)
      }
    },
    getSlideBackground(slide) {
      if (slide.background.type === 'image') {
        return {
          backgroundImage: `url(${slide.background.value})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center center',
          backgroundRepeat: 'no-repeat',
          backgroundAttachment: 'fixed'
        }
      } else {
        return {
          background: slide.background.value
        }
      }
    },
    getLayoutStyle(layout) {
      return {
        flexDirection: layout.direction,
        textAlign: layout.textAlign,
        width: layout.contentWidth
      }
    },
    getImageStyle(slide) {
      return {
        width: slide.layout.imageWidth,
        order: slide.layout.imagePosition === 'bottom' ? 2 : 1
      }
    },
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.sliderData.slides.length
    },
    prevSlide() {
      this.currentSlide = this.currentSlide === 0 ? this.sliderData.slides.length - 1 : this.currentSlide - 1
    },
    goToSlide(index) {
      this.currentSlide = index
    },
    startAutoplay() {
      this.autoplayInterval = setInterval(() => {
        this.nextSlide()
      }, this.sliderData.settings.autoplayDelay)
    },
    stopAutoplay() {
      if (this.autoplayInterval) {
        clearInterval(this.autoplayInterval)
      }
    },
    handleMouseEnter() {
      if (this.sliderData.settings.pauseOnHover) {
        this.stopAutoplay()
      }
    },
    handleMouseLeave() {
      if (this.sliderData.settings.pauseOnHover && this.sliderData.settings.autoplay) {
        this.startAutoplay()
      }
    }
  }
}
</script>

<style scoped>
.hero-slider {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.slider-container {
  position: relative;
  width: 100%;
  height: 100%;
}

.slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 1.2s ease-in-out;
  display: flex;
  align-items: center;
  justify-content: center;
  /* Ensure background covers entire slide */
  background-size: cover !important;
  background-position: center center !important;
  background-repeat: no-repeat !important;
}

.slide.active {
  opacity: 1;
}

.slide-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1;
  /* Stronger overlay for better text readability */
  background: rgba(0, 0, 0, 0.5) !important;
}

.slide-content {
  position: relative;
  z-index: 2;
  color: white;
  max-width: 1200px;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  width: 100%;
}

.content-wrapper {
  flex: 1;
  max-width: 600px;
}

.slide-title {
  margin-bottom: 1rem;
  line-height: 1.2;
}

.slide-subtitle {
  margin-bottom: 1.5rem;
}

.slide-description {
  margin-bottom: 2.5rem;
}

.slide-buttons {
  display: flex;
  gap: 1rem;
  justify-content: flex-start;
  flex-wrap: wrap;
}

.slide-image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slide-image img {
  max-width: 100%;
  height: auto;
}

.slider-dots {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  z-index: 3;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.7);
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  background: white;
  border-color: white;
}

.dot:hover {
  background: rgba(255, 255, 255, 0.8);
}

.navigation-arrows {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 3;
}

.nav-arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255, 255, 255, 0.15);
  border: 2px solid rgba(255, 255, 255, 0.3);
  color: white;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
  pointer-events: auto;
}

.nav-arrow:hover {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.6);
  transform: translateY(-50%) scale(1.1);
}

.nav-arrow.prev {
  left: 30px;
}

.nav-arrow.next {
  right: 30px;
}

/* Responsive Design */
@media (max-width: 768px) {
  .slide-content {
    flex-direction: column !important;
    text-align: center !important;
  }
  
  .slide-buttons {
    justify-content: center;
  }
  
  .navigation-arrows {
    position: absolute !important;
    
    left: 0 !important;
    right: 0 !important;
    transform: none !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: flex-end !important;
    padding: 0 20px !important;
    gap: 0 !important;
  }
  
  .nav-arrow {
    position: relative;
    top: auto;
    left: auto;
    right: auto;
    transform: none;
    width: 45px;
    height: 45px;
    margin: 0;
  }
  
  .nav-arrow.prev {
    left: auto;
  }
  
  .nav-arrow.next {
    right: auto;
  }
  
  .slider-dots {
    bottom: 20px;
  }
  
  .dot {
    width: 10px;
    height: 10px;
  }
}

@media (max-width: 480px) {
  .slide-content {
    padding: 0 15px;
  }
  
  .slide-buttons {
    flex-direction: column;
    align-items: center;
  }
  
  .slide-buttons .v-btn {
    min-width: 200px;
  }
  
  .navigation-arrows {
    bottom: 15px !important;
    padding: 0 15px !important;
  }
  
  .nav-arrow {
    width: 40px;
    height: 40px;
    margin: 0;
  }
}
</style>