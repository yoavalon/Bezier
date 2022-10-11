d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)

d.end()
