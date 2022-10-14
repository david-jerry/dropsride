import Swiper from "swiper";


export default function SwiperComponent() {
    return {
        swiper: null,
        initSwiper() {
            this.swiper = new Swiper(this.$refs.swiper, {
                slidesPerView: 1,
                spaceBetween: 10,
                speed: 1000,
                loop: true,
                pagination: {
                    el: this.$refs.swiperPagination,
                    clickable: true,
                },
                navigation: {
                    nextEl: this.$refs.swiperNext,
                    prevEl: this.$refs.swiperPrev,
                },
                autoplay: {
                    delay: 5000,
                    disableOnInteraction: false,
                },
                breakpoints: {
                    320: { slidesPerView: 1, spaceBetween: 20 },
                    480: { slidesPerView: 1, spaceBetween: 30 },
                    640: { slidesPerView: 2, spaceBetween: 40 },
                    768: { slidesPerView: 3, spaceBetween: 30 },
                    1524: { slidesPerView: 4, spaceBetween: 30 },
                },
            });
        },
        nextSlide() {
            this.swiper.slideNext();
        },
        prevSlide() {
            this.swiper.slidePrev();
        }
    };
}



