d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)

d.end()
