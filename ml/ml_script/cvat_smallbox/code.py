from xml.etree import ElementTree as ET
import logging
import click


def get_segments_root(root, v=False):
    try:
        segments = []
        for i in root.iter('segment'):
            o = {}
            for j in i:
                o[f'{j.tag}'] = j.text
            segments.append(o)
        if v:
            click.echo(click.style('--- segments created :) ', fg='bright_cyan', bold=True))
        return segments
    except Exception as e:
        logging.error(e.__str__())


def read_xml(in_file, v=False):
    """
    open xml file and return root  iterate file
    """

    try:
        tree = ET.parse(in_file)
        if v:
            click.echo(click.style('--- xml readed :) ', fg='bright_cyan', bold=True))
        return tree.getroot()
    except Exception as e:
        logging.error(e.__str__())


@click.command()
@click.option("--in", "-i", "in_file", required=True, help="Path to xml cvt file to be processed.", )
@click.option("--toleranci", "-t", default=1.0,
              help="toleranci to filter box area, default 1 (1% area of image).")
def process(in_file, toleranci):
    """
    Processes the area of cvt file and filter small boxes
    """
    # vars
    # function_name = 'SMALLBOX'
    # path = os.path.dirname(in_file)
    # file_name = os.path.basename(in_file)
    toleranci = toleranci / 100
    # ouput_file_name = f'{file_name.lower().replace(".xml", "")}_{function_name}_OUTPUT.csv'
    list_image_err = [['url', 'id-image', 'area', ]]

    root = read_xml(in_file)

    segments = get_segments_root(root)

    try:
        for i in root:
            if i.tag == 'image':
                url = ''
                image_id = int(i.get('id'))
                for j in segments:
                    if int(j.get('start')) <= image_id <= int(j.get('stop')):
                        url = j.get('url')
                area_imagen = float(float(i.get('width')) * float(i.get('height'))).__round__(3)

                for j in i:
                    if j.tag == 'box':
                        image = [f'{url}&frame={i.get("id")}', int(i.get('id'))]
                        x = abs(float(j.get('xbr')) - float(j.get('xtl')))
                        y = abs(float(j.get('ybr')) - float(j.get('ytl')))
                        a_box = float(x * y).__round__(3)
                        image.append(a_box)

                        if (a_box / area_imagen) <= toleranci:
                            list_image_err.append(image)


    except Exception as e:
        logging.error(e.__str__())
    else:
        # save_csv(ouput_file_name, list_image_err,ouput_path)
        # df = DataFrame(list_image_err)
        # print version
        for i in list_image_err:
            print(f'{i[0]},{i[1]},{i[2]}')


if __name__ == '__main__':
    process()