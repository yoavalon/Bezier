d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.medium)

d.end()
