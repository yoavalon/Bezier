d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.long)
d.position_pen(0,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)

d.end()
