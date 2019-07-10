# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 19:32:41 2019

@author: admin
"""

article_text = """
The Green New Deal Is What Realistic Environmental Policy Looks Like

Feb. 14, 2019

Everyone is lining up to endorse the Green New Deal — or to mock it.
Kamala Harris, Cory Booker, Bernie Sanders, Elizabeth Warren and
Kirsten Gillibrand have all endorsed the resolution sponsored by
Representative Alexandria Ocasio-Cortez of New York and Senator Edward
Markey of Massachusetts.

Conservative critics predictably call it “a shocking document” and “a
call for enviro-socialism in America,” but liberal condescension has
cut deeper. The House speaker, Nancy Pelosi, essentially dismissed it
as branding, saying, “The green dream, or whatever they call it,
nobody knows what it is, but they’re for it, right?” Others have
criticized it for leaving out any mention of a carbon tax, a
cornerstone of mainstream climate-policy proposals, while embracing a
left-populist agenda that includes universal health care, stronger
labor rights and a jobs guarantee.

What do these goals have to do with stabilizing atmospheric carbon
levels before climate change makes large parts of the world
uninhabitable? What has taken liberal critics aback is that the Green
New Deal strays so far from the traditional environmental emphasis on
controlling pollution, which the carbon tax aims to do, and tries to
solve the problems of economic inequality, poverty and even corporate
concentration (there’s an antimonopoly clause).

But this everything-and-the-carbon-sink strategy is actually a feature
of the approach, not a bug, and not only for reasons of ideological
branding. In the 21st century, environmental policy is economic
policy. Keeping the two separate isn’t a feat of intellectual
discipline. It’s an anachronism.

Our carbon emissions are not mainly about the price of gasoline or
electricity. They’re about infrastructure. For every human being,
there are over 1,000 tons of built environment: roads, office
buildings, power plants, cars and trains and long-haul trucks. It is a
technological exoskeleton for the species. Everything most of us do,
we do through it: calling our parents, getting to work, moving for a
job, taking the family on vacation, finding food for the evening or
staying warm in a polar vortex. Just being human in this artificial
world implies a definite carbon footprint — and for that matter, a
trail of footprints in water use, soil compaction, habitat degradation
and pesticide use. You cannot change the climate impact of Americans
without changing the built American landscape.

So the proposals to retrofit buildings, retool transportation and
build a clean-energy system are simply ways of tackling the problem
where it starts. They are public-works projects because large capital
projects — especially ones that, like highways, involve widespread
public benefit — have always required public money. They are jobs
programs, unless robots do the work, so the jobs might as well be
good.

The deeper point is that any economic policy is a jobs policy. The oil
and gas sector provides at least 1.4 million American jobs, more if
you believe industry estimates, and depends on public subsidies and
infrastructure. You might say that producing the disaster of global
climate change has taken a lot of economic policy and produced a lot
of jobs programs. Reversing direction will take the same. Since
environmental policy can happen only through economic policy, there is
no avoiding decisions about what sorts of work there will be, and in
which industries. It’s unsettling, but maybe a little less so when you
consider that we’ve been doing it all along, usually without owning up
to it.

Take the Green New Deal’s proposal to work with family farmers and
ranchers to reduce the carbon footprint of agriculture. It might sound
like a sop to rural representatives, the locavore caucus of the
Democratic Socialists of America, or both. (And that wouldn’t make it
wrong.) But food is our everyday metabolism with the natural world,
which is why agriculture emits 9 percent of United States carbon,
according to the Environmental Protection Agency. (Other estimates are
considerably higher.)

Forty percent of our land is farmed or ranched, which is to say, the
soil is basically conscripted as a food factory. The food system is
already pervasively shaped by the Farm Bill, which spends nearly $15
billion per year on subsidies and $10 billion on conservation
measures, deeply shaping what farmers grow and where, and tending to
benefit large, industrially oriented operations. Food production can
be much less carbon-intensive with changed practices in cropping,
fertilizing, irrigation and waste management, many of them well suited
to small farming. Moving in that direction, though, would require
rattling the cage of big American agriculture.

As with energy, getting lawmaking involved wouldn’t be new. It has
taken years of agricultural policy to get us into this mess. Getting
out of it is a question not of whether lawmaking also produces
economic policy and jobs, but of what kind.

The Green New Deal isn’t the only approach, of course, but its broad
ambitions mark out the ground where future climate fights will happen.
Because reshaping our environmental impact means reworking our
economy, there will inevitably be competing visions about who deserves
to benefit and what kind of economy we should build. Centrist
proposals will concentrate on promoting investment in new
technologies, with profits going, pharma-style, to private researchers
and manufacturers.

If Trumpist nationalism outgrows its climate denialism but survives to
fight again, it will double down on supporting national energy
industries and denying the ethical responsibilities of global
interdependence by building border walls against climate refugees. To
the left of the Green New Deal, there will be louder calls to
nationalize fossil fuels in order to leave them in the ground. (A
carbon tax would be compatible with any of these visions, depending on
who paid it and how the revenues were spent.)

Curiously, the idea that environmental policy could ever be separated
from the larger economic order, or from fights over fairness, is
recent, a product of an unusually technocratic period in American
politics. Arguing for the Clean Air Act on Earth Day 1970, Senator
Edmund Muskie, Democrat of Maine and the law’s lead drafter, insisted
that “man’s environment” included “the shape of the communities in
which he lives” and that “the only kind of society that has a chance”
was “a society that will not tolerate slums for some and decent houses
for others, rats for some and playgrounds for others, clean air for
some and filth for others.”

For Senator Muskie, environmentalism meant that no neighborhood or job
should be toxic. In the three years that followed, the country adopted
the most ambitious and effective environmental legislation in its
history, including Mr. Muskie’s Clean Air Act, the Clean Water Act and
the Endangered Species Act. Mr. Muskie’s approach remains a model of
visionary environmental lawmaking. Like much new radicalism, the Green
New Deal is good sense rediscovered.

"""
wordCount = len(article_text)
print(wordCount)
def checkGreen(string):
    if string.lower() == "green":
        return True
    else:
        return False
    
for i in range(1,wordCount-5):
    string = article_text[i:i+5]
    check = checkGreen(string)
    if check == True:
        article_text = article_text[:i] + "red" + article_text[i+5:]
        
print(article_text)