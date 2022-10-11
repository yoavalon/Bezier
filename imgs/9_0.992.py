d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(3,1)

d.end()
