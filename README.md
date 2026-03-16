# 🎓 SkillAgent

> Entrenador corporativo agéntico para capacitación en AI — $20/persona/mes

**El coach de AI que tu equipo necesita, disponible 24/7, al costo de un almuerzo por persona.**

---

## ¿Qué es SkillAgent?

SkillAgent es una plataforma de capacitación corporativa donde cada empleado tiene su propio entrenador de AI personalizado. No es un curso en video que nadie termina. Es un agente conversacional que adapta las lecciones a tu rol, responde preguntas, evalúa tu progreso y te certifica.

**Problema:** El 89% de los empleados de PyMEs mexicanas nunca han recibido capacitación formal en AI. Sus empresas saben que necesitan adoptar AI pero no saben por dónde empezar ni tienen presupuesto para consultoras.

**Solución:** SkillAgent democratiza la capacitación en AI — $20/persona/mes, sin instalaciones, sin consultores, sin excusas.

---

## ¿Cómo funciona?

### Para el Admin de la empresa:
1. Crea tu cuenta y registra tu empresa
2. Invita a tu equipo por email (tantos como necesites)
3. Asigna rutas de aprendizaje por rol o área
4. Monitorea el progreso desde tu dashboard

### Para el empleado:
1. Entra con tu email
2. Tu entrenador personal te da la bienvenida
3. Completa lecciones conversacionales (no videos, no PDFs aburridos)
4. Responde evaluaciones y gana badges
5. Aplica lo aprendido en tu trabajo al día siguiente

---

## Módulos de Aprendizaje

### Módulo 1: AI para tu trabajo diario *(disponible ahora)*
- Lección 1: ¿Qué es AI y cómo afecta tu rol?
- Lección 2: Prompting efectivo para no técnicos
- Lección 3: Herramientas AI que puedes usar hoy

### Próximos módulos:
- Módulo 2: Automatización sin código con AI
- Módulo 3: AI para ventas y atención a clientes
- Módulo 4: AI para contabilidad y finanzas
- Módulo 5: Seguridad y ética en el uso de AI

---

## Tech Stack

| Capa | Tecnología |
|------|-----------|
| Frontend | Next.js 14 + TypeScript + Tailwind CSS |
| Animaciones | Framer Motion |
| UI Components | shadcn/ui |
| Backend | Next.js API Routes |
| Base de datos | Supabase (Postgres + Auth + Realtime) |
| AI Principal | Claude 3.5 Sonnet (Anthropic) |
| AI Evaluaciones | Groq + Llama 3.1 70B (menor latencia) |
| Billing | Stripe (per-seat, $20 USD/persona/mes) |
| Rate Limiting | Upstash Redis |
| Deploy | Vercel |
| Email | Resend |

### Arquitectura de AI
- **Claude** → Conversaciones de aprendizaje, explicaciones profundas, feedback personalizado
- **Groq/Llama** → Evaluaciones rápidas, quizzes, respuestas cortas (10x más rápido, menor costo)
- Estrategia: usar el modelo correcto para cada tarea

---

## Estructura del Proyecto

```
skillagent/
├── app/
│   ├── page.tsx                          # Landing
│   ├── (auth)/
│   │   ├── login/page.tsx
│   │   └── registro/page.tsx
│   ├── (app)/
│   │   ├── dashboard/page.tsx            # Dashboard empleado
│   │   ├── modulos/
│   │   │   ├── page.tsx                  # Catálogo de módulos
│   │   │   └── [slug]/
│   │   │       ├── page.tsx              # Módulo overview
│   │   │       └── leccion/[id]/page.tsx # Lección con tutor AI
│   │   └── admin/
│   │       ├── page.tsx                  # Dashboard admin
│   │       ├── equipo/page.tsx           # Gestión de usuarios
│   │       └── progreso/page.tsx         # Reportes
│   └── api/
│       ├── chat/route.ts                 # Claude conversacional
│       ├── evaluar/route.ts              # Evaluación Groq
│       └── progreso/route.ts             # Tracking
├── components/
│   ├── LeccionViewer.tsx
│   ├── ChatTutor.tsx                     # Interfaz del tutor AI
│   ├── QuizEvaluador.tsx
│   └── DashboardAdmin.tsx
├── lib/
│   ├── claude.ts
│   ├── groq.ts
│   ├── supabase.ts
│   └── stripe.ts
├── content/
│   └── modulos/
│       └── modulo-01-ai-para-tu-trabajo/
│           ├── meta.json
│           ├── leccion-01.md
│           ├── leccion-02.md
│           └── leccion-03.md
└── prompts/
    ├── tutor-system.ts                   # System prompt del coach
    └── evaluador.ts                      # Prompt de evaluación
```

---

## Configuración

```bash
git clone https://github.com/franduranv/skillagent.git
cd skillagent
npm install
cp .env.example .env.local
npm run dev
```

### Variables de entorno

```env
ANTHROPIC_API_KEY=
GROQ_API_KEY=
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
RESEND_API_KEY=
UPSTASH_REDIS_REST_URL=
UPSTASH_REDIS_REST_TOKEN=
```

---

## Pricing

| Plan | Precio | Incluye |
|------|--------|---------|
| **Starter** | $20 USD/persona/mes | Todos los módulos, dashboard admin, soporte email |
| **Growth** | $15 USD/persona/mes | +5 seats mínimo, reportes avanzados |
| **Enterprise** | Custom | Contenido personalizado, integración Slack/Teams |

---

## Roadmap

### v0.1 — MVP (48h)
- [x] Auth multi-tenant (empresa + empleados)
- [x] Módulo 1 completo (3 lecciones)
- [x] Chat con tutor Claude
- [x] Evaluación al final de cada lección
- [x] Dashboard admin básico

### v0.2 — Beta
- [ ] Billing con Stripe (per-seat)
- [ ] Onboarding automatizado por email
- [ ] Módulos 2 y 3
- [ ] Certificados de completado

### v1.0 — Producción
- [ ] Integración Slack (bot de micro-aprendizaje diario)
- [ ] Integración WhatsApp Business
- [ ] Contenido personalizado por industria
- [ ] API para ERPs y HRIS (Workday, SAP)

---

## ¿Por qué SkillAgent en lugar de cursos en video?

| | Videos tradicionales | SkillAgent |
|--|---------------------|-----------|
| Completación | ~15% | >75% (conversacional = engagement) |
| Adaptación | Fija | Se adapta al rol del empleado |
| Disponibilidad | Horario plataforma | 24/7 |
| Evaluación | Quiz genérico | Evaluación contextualizada por Claude |
| Costo por empleado | $50-200/mes | $20/mes |

---

## Parte de ZXY Ventures

SkillAgent es un proyecto de **[ZXY Ventures](https://zxy.vc)** — venture studio construyendo el futuro de las PyMEs mexicanas con AI.

**Contacto:** fran@zxy.vc

---

*Built with ❤️ in León, Guanajuato, México 🇲🇽*
