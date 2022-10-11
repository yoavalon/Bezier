d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.position_pen(3,0)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.long)

d.end()
