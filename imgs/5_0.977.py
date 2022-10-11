d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.long)
d.position_pen(3,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.position_pen(3,0)
d.straight_line(Direction.E, Length.medium)

d.end()
