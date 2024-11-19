document.addEventListener('DOMContentLoaded', () => {
    // Fade-in sections
    const sections = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            }
        });
    }, { threshold: 0.2 });

    sections.forEach(section => observer.observe(section));

    // Animate skills progress bars
    const skillsSection = document.querySelector('#skills');
    const skillBars = document.querySelectorAll('.progress-bar');

    const skillObserver = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                skillBars.forEach(bar => {
                    const skillWidth = bar.getAttribute('data-skill');
                    bar.style.setProperty('--width', skillWidth);
                });
                skillObserver.unobserve(entry.target); // Stop observing once animation has triggered
            }
        });
    }, { threshold: 0.5 });

    if (skillsSection) {
        skillObserver.observe(skillsSection);
    }
});
