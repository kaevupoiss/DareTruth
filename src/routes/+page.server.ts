import type { PageServerLoad } from './$types';
import type { Actions } from './$types';
import dares from '$lib/dares.json';

export const load: PageServerLoad = (async () => {
    return {};
})

export const actions = {
    default: async ({ request }) => {
        const data = await request.formData()

        const level = Number(data.get('level'))
        const tod = data.get('tod')

        if (!level || !tod) {
            return
        }

        if (tod !== 'truths' && tod !== 'dares') {
            return
        }

        const levelItems = dares.levels[level - 1]
        const daresToChooseFrom = levelItems[tod]

        let newDare = daresToChooseFrom[Math.floor(Math.random() * daresToChooseFrom.length)]

        console.log();
        

        if (level >= 2) {
            const chance = Math.floor(Math.random() * 100);

            if (chance <= 2 * (level - 2))
                newDare = "Special Dare: Remove one piece of clothing"
        }

        return { newDare, level }
    }
} satisfies Actions;
