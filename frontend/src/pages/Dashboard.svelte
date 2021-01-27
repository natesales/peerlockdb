<script>
    import {
        Breadcrumb,
        BreadcrumbItem,
    } from "carbon-components-svelte/src/Breadcrumb";
    import {Grid, Row, Column} from "carbon-components-svelte/src/Grid";
    import {Tabs, TabContent, Tab} from "carbon-components-svelte/src/Tabs";
    import {Select, SelectItem} from "carbon-components-svelte/src/Select";
    import {DataTable} from "carbon-components-svelte/src/DataTable";
    import {theme} from "../stores";
</script>

<main>
    <Grid>
        <Row>
            <Column lg="{16}">
                <Breadcrumb aria-label="Page navigation" noTrailingSlash>
                    <BreadcrumbItem href="/">Getting started</BreadcrumbItem>
                </Breadcrumb>
                <h1 style="margin-bottom: 1.5rem">PeerlockDB</h1>
            </Column>
        </Row>

        <Row>
            <Column noGutter>
                <Tabs aria-label="Tab navigation">
                    <Tab label="About"/>
                    <Tab label="Design"/>
                    <Tab label="Develop"/>
                    <div class="tabbed-content" slot="content">
                        <Grid as fullWidth let:props>
                            <TabContent {...props}>
                                <Row>
                                    <Column lg="{7}" md="{4}">
                                        <Select
                                                bind:selected="{$theme}"
                                                labelText="Carbon theme"
                                                style="margin-bottom: 1rem"
                                        >
                                            <SelectItem text="White" value="white"/>
                                            <SelectItem text="Gray 10" value="g10"/>
                                            <SelectItem text="Gray 90" value="g90"/>
                                            <SelectItem text="Gray 100" value="g100"/>
                                        </Select>
                                        <p>
                                            Carbon is IBM’s open-source design system for digital
                                            products and experiences. With the IBM Design Language
                                            as its foundation, the system consists of working code,
                                            design tools and resources, human interface guidelines,
                                            and a vibrant community of contributors.
                                        </p>
                                    </Column>
                                </Row>
                            </TabContent>
                            <TabContent {...props}>
                                <Row>
                                    <Column lg="{7}" md="{4}">
                                        <DataTable
                                                headers={[{ key: 'name', value: 'Name' }, { key: 'protocol', value: 'Protocol' }, { key: 'port', value: 'Port' }, { key: 'rule', value: 'Rule' }]}
                                                rows={[{ id: 'a', name: 'Load Balancer 3', protocol: 'HTTP', port: 3000, rule: 'Round robin' }, { id: 'b', name: 'Load Balancer 1', protocol: 'HTTP', port: 443, rule: 'Round robin' }, { id: 'c', name: 'Load Balancer 2', protocol: 'HTTP', port: 80, rule: 'DNS delegation' }, { id: 'd', name: 'Load Balancer 6', protocol: 'HTTP', port: 3000, rule: 'Round robin' }, { id: 'e', name: 'Load Balancer 4', protocol: 'HTTP', port: 443, rule: 'Round robin' }, { id: 'f', name: 'Load Balancer 5', protocol: 'HTTP', port: 80, rule: 'DNS delegation' }]}
                                        >
                                        </DataTable>
                                    </Column>
                                </Row>
                            </TabContent>
                            <TabContent {...props}>
                                <Row>
                                    <Column lg="{7}" md="{4}">
                                        <p>
                                            Carbon provides styles and components in Vanilla, React,
                                            Angular, Vue and Svelte for anyone building on the web.
                                        </p>
                                    </Column>
                                </Row>
                            </TabContent>
                        </Grid>
                    </div>
                </Tabs>
            </Column>
        </Row>
    </Grid>
</main>
