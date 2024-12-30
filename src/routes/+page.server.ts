import { prisma } from '$lib/utils/prisma';
import type { Actions, PageServerLoad } from './$types';
import { v4 } from 'uuid'


export const actions = {
    submitFeedback: async ({ request, locals, params }) => {
        const formData = await request.formData()

        const message = formData.get('message') as string

        if (message) {

            const uuidv4 = v4()

            const data = await prisma.feedback.create({
                data: {
                    uuid: uuidv4,
                    message: message
                }
            })

            return {
                message: 'Success'
            }

        }
    }
} satisfies Actions