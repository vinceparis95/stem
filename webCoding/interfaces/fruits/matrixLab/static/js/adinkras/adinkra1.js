

///////////////////////////////////////////

var adinkra = anime.timeline({
    loop:true,
  duration:361
})

///////////////////////////////////////////


adinkra
    .add({
    // loop: true,
    targets: '.container50',
    translateY: -250,
    rotate: {value: 45},
    height: {
      value: '*=3',
      easing: 'easeInOutQuad'
    },
    width: 19,
    // autoplay: true,
  })


    .add({
    // loop: true,
    targets: '.container51',
    translateY: -250,
    rotate: {value: -45},
    height: {
      value: '*=3',
      easing: 'easeInOutQuad'
    },
    width: 19,
    // autoplay: true

  })
    .add({
    // loop: true,
    targets: '.container52',
    translateY: -250,
    rotate: {value: -45},
    height: {
      value: '*=3',
      easing: 'easeInOutQuad'
    },
    width: 19,
    // autoplay: true

  });

adinkra
    .add({
      // loop: true,
      targets: '.container53',
      translateY: [-250],
      rotate: {value: 45},
      height: {
        value: '*=3',
        easing: 'easeInOutQuad'},
      width: 19,
      // autoplay: true
    })


    //////////////////////////////////////////
    //Folding

    .add({
      targets: '.container53',
      rotate: {value: 180},
      translateX: [63]
    })

    .add({
      targets: '.container52',
      rotate: {value: 180},
      translateX: [-63]
    })
    .add({
      targets: '.container51',
      rotate: {value: 180},
      translateX: [67],

    })
    .add({
      targets: '.container50',
      rotate: {value: 180},
      translateX: [-63]
    });

/////////////////////////////////////////

//folding again

adinkra
    .add({
          targets: '.container50',
          translateY: [-200],
          easing: 'easeInOutSine'
        }
    )
    .add({
          targets: '.container51',
          translateY: [-200],
          easing: 'easeInOutSine'
        }
    )
    .add({
          targets: '.container52',
          easing: 'easeInOutSine',
      translateY: [-320],

        }
    )
    .add({
          targets: '.container53',
          easing: 'easeInOutSine',
                translateY: [-320],
        }
    );



