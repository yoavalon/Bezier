d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SE, Length.long)

d.end()
