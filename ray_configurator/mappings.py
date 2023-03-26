setting = {
    'SUN_LIGHT_ENABLE': {
        0: "Disabled",
        1: "Enabled"
    },
    'SUN_SHADOW_MAP_QUALITY': {
        0: "Disabled",
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Ultra"
    },
    'SUN_SHADOW_SAMPLE_QUALITY': {
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Low w/ PCSS",
        5: "Medium w/ PCSS",
        6: "High w/ PCSS"
    },
    'SUN_CONTACT_SHADOW_QUALITY': {
        0: "Enabled",
        1: "Disabled"
    },
    'MULTI_LIGHT_ENABLE': {
        0: "Enabled",
        1: "Disabled"
    },
    'MULTI_SHADOW_MAP_QUALITY': {
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Ultra"
    },
    'MULTI_SHADOW_SAMPLE_QUALITY': {
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Low w/ PCSS",
        5: "Medium w/ PCSS",
        6: "High w/ PCSS"
    },
    'MULTI_VOLUMETRIC_LIGHT_QUALITY': {
        0: "Disabled",
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Ultra"
    },
    'MULTI_VOLUMETRIC_SHADOW_QUALITY': {
        0: "Disabled",
        1: "Low",
        2: "Medium",
        3: "High",
        4: "Ultra"
    },
    'IBL_QUALITY': {
        0: "Disabled",
        1: "Enabled",
        2: "Enabled w/ UV flip"
    },
    'FOG_ENABLE': {
        0: "Disabled",
        1: "Enabled"
    },
    'OUTLINE_QUALITY': {
        0: "Disabled",
        1: "Enabled",
        2: "Enabled + SSAA"
    },
    'TOON_ENABLE': {
        0: "Disabled",
        1: "Enabled",
        2: "Enabled w/ Diffusion"
    },
    'SSDO_QUALITY': {
        0: "Disabled",
        1: "16 samples",
        2: "24 samples",
        3: "32 samples",
        4: "48 samples",
        5: "64 samples",
        6: "80 samples",
    },
    'SSR_QUALITY': {
        0: "Disabled",
        1: "32 samples",
        2: "64 samples",
        3: "128 samples",
    },
    'SSSS_QUALITY': {
        0: "Disabled",
        1: "Enabled",
    },
    'SSGI_QUALITY': {
        0: "Disabled",
        1: "16 samples",
        2: "24 samples",
        3: "32 samples",
        4: "48 samples",
        5: "64 samples",
        6: "80 samples",
    },
    'BOKEH_MODE': {
        0: "Disabled",
        1: "Cinematic",
        2: "Hexagonal",
    },
    'EYE_ADAPTATION': {
        0: "Disabled",
        1: "ISO 100",
    },
    'BLOOM_MODE': {
        0: "Disabled",
        1: "Enabled",
    },
    'BLOOM_DIRT_ENABLE': {
        0: "Disabled",
        1: "Enabled",
    },
    'HDR_STAR_MODE': {
        0: "Disabled",
        1: "Anamorphic Lens Flares (Blue)",
        2: "Anamorphic Lens Flares (Auto)",
        3: "Glare Star (Orange)",
        4: "Glare Star (Auto)",
    },
    'HDR_TONEMAP_OPERATOR': {
        0: "Linear",
        1: "Reinhard",
        2: "John-Hable",
        3: "Neutral",
        4: "Hejl2015",
        5: "ACES",
        6: "Naughty Dog",
    },
    'AA_QUALITY': {
        0: "Disabled",
        1: "FXAA",
        2: "SMAAx1 (Medium)",
        3: "SMAAx1 (High)",
        4: "SMAAx2 (Medium)",
        5: "SMAAx2 (High)",
    },
    'POST_DISPERSION_MODE': {
        0: "Disabled",
        1: "Colour Shift",
        2: "Chromatic Aberration",
    }
}

name = {
    'SUN_LIGHT_ENABLE': 'Sun Light',
    'SUN_SHADOW_MAP_QUALITY': 'Cascade Shadow Map Quality',
    'SUN_SHADOW_SAMPLE_QUALITY': 'Cascade Shadow Sample Count',
    'SUN_CONTACT_SHADOW_QUALITY': 'Screen Space Contact Shadow',
    'MULTI_LIGHT_ENABLE': 'Light Tab',
    'MULTI_SHADOW_MAP_QUALITY': 'Shadow Map Quality',
    'MULTI_SHADOW_SAMPLE_QUALITY': 'Shadow Sample Count',
    'MULTI_VOLUMETRIC_LIGHT_QUALITY': 'Volumetric Light Setting',
    'MULTI_VOLUMETRIC_SHADOW_QUALITY': 'Volumetric Shadow Map Setting',
    'IBL_QUALITY': 'Image Based Lighting',
    'FOG_ENABLE': 'Fog Tab',
    'OUTLINE_QUALITY': 'Outline Tab',
    'TOON_ENABLE': 'Toon Shading Material',
    'SSDO_QUALITY': 'Horizon Based Ambient Occlusion Plus (SSDO)',
    'SSR_QUALITY': 'Screen Space Reflection',
    'SSSS_QUALITY': 'Subsurface Scattering',
    'SSGI_QUALITY': 'Screen Space Global Illumination',
    'BOKEH_MODE': 'Bokeh Depth of Field',
    'EYE_ADAPTATION': 'Eye Adaptation',
    'BLOOM_MODE': 'Bloom',
    'BLOOM_DIRT_ENABLE': 'Bloom Dirt Mask',
    'HDR_STAR_MODE': 'Lens Flare/Star',
    'HDR_TONEMAP_OPERATOR': 'Tonemapper',
    'AA_QUALITY': 'Anti-Aliasing',
    'POST_DISPERSION_MODE': 'Post Dispersion',
}

category = {
    'Lighting': ['SUN_LIGHT_ENABLE', 'MULTI_LIGHT_ENABLE', 'IBL_QUALITY', 'MULTI_VOLUMETRIC_LIGHT_QUALITY', 'EYE_ADAPTATION'],
    'Shadows': ['SUN_SHADOW_MAP_QUALITY', 'SUN_SHADOW_SAMPLE_QUALITY', 'MULTI_SHADOW_MAP_QUALITY', 'MULTI_SHADOW_SAMPLE_QUALITY', 'MULTI_VOLUMETRIC_SHADOW_QUALITY'],
    'Fog': ['FOG_ENABLE'],
    'Outline': ['OUTLINE_QUALITY'],
    'Toon': ['TOON_ENABLE'],
    'Effects': ['SSDO_QUALITY', 'SSSS_QUALITY', 'BOKEH_MODE', 'BLOOM_MODE', 'BLOOM_DIRT_ENABLE', 'HDR_STAR_MODE', 'HDR_TONEMAP_OPERATOR', 'AA_QUALITY', 'POST_DISPERSION_MODE'],
    'Experimental': ['SSGI_QUALITY', 'SSR_QUALITY', 'SUN_CONTACT_SHADOW_QUALITY']
}

inputs = {
    'SUN_LIGHT_ENABLE': 'checkbox',
    'SUN_SHADOW_MAP_QUALITY': 'dropdown',
    'SUN_SHADOW_SAMPLE_QUALITY': 'dropdown',
    'SUN_CONTACT_SHADOW_QUALITY': 'checkbox',
    'MULTI_LIGHT_ENABLE': 'checkbox',
    'MULTI_SHADOW_MAP_QUALITY': 'dropdown',
    'MULTI_SHADOW_SAMPLE_QUALITY': 'dropdown',
    'MULTI_VOLUMETRIC_LIGHT_QUALITY': 'dropdown',
    'MULTI_VOLUMETRIC_SHADOW_QUALITY': 'dropdown',
    'IBL_QUALITY': 'dropdown',
    'FOG_ENABLE': 'checkbox',
    'OUTLINE_QUALITY': 'dropdown',
    'TOON_ENABLE': 'dropdown',
    'SSDO_QUALITY': 'dropdown',
    'SSR_QUALITY': 'dropdown',
    'SSSS_QUALITY': 'checkbox',
    'SSGI_QUALITY': 'dropdown',
    'BOKEH_MODE': 'dropdown',
    'EYE_ADAPTATION': 'dropdown',
    'BLOOM_MODE': 'checkbox',
    'BLOOM_DIRT_ENABLE': 'checkbox',
    'HDR_STAR_MODE': 'dropdown',
    'HDR_TONEMAP_OPERATOR': 'dropdown',
    'AA_QUALITY': 'dropdown',
    'POST_DISPERSION_MODE': 'dropdown',
}

defaults = {
    'SUN_LIGHT_ENABLE': 1,
    'SUN_SHADOW_MAP_QUALITY': 3,
    'SUN_SHADOW_SAMPLE_QUALITY': 2,
    'SUN_CONTACT_SHADOW_QUALITY': 1,
    'MULTI_LIGHT_ENABLE': 1,
    'MULTI_SHADOW_MAP_QUALITY': 1,
    'MULTI_SHADOW_SAMPLE_QUALITY': 5,
    'MULTI_VOLUMETRIC_LIGHT_QUALITY': 1,
    'MULTI_VOLUMETRIC_SHADOW_QUALITY': 1,
    'IBL_QUALITY': 1,
    'FOG_ENABLE': 1,
    'OUTLINE_QUALITY': 1,
    'TOON_ENABLE': 1,
    'SSDO_QUALITY': 2,
    'SSR_QUALITY': 1,
    'SSSS_QUALITY': 1,
    'SSGI_QUALITY': 0,
    'BOKEH_MODE': 1,
    'EYE_ADAPTATION': 0,
    'BLOOM_MODE': 1,
    'BLOOM_DIRT_ENABLE': 1,
    'HDR_STAR_MODE': 0,
    'HDR_TONEMAP_OPERATOR': 3,
    'AA_QUALITY': 1,
    'POST_DISPERSION_MODE': 1,
}
