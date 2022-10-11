d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
