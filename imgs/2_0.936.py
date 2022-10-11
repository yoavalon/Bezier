d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(3,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)

d.end()
